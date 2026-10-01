"""Run with python3 -B -m unittest discover -s tests -v.

All tests use temporary databases and uploads, never the project's saved data.
"""
import io
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from flask import Flask
from sqlalchemy.exc import SQLAlchemyError

from config import Config
from extensions import db
from models.jobApplication import JobApplication
from models.jobopening import JobOpening
from routes.pages import pages_bp
from scripts.repair_job_applications import repair


class CareersTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        project = Path(__file__).resolve().parents[1]
        self.app = Flask(__name__, template_folder=str(project / 'templates'))
        self.app.config.from_object(Config)
        self.app.config.update(
            TESTING=True, SECRET_KEY='test-only', SQLALCHEMY_DATABASE_URI='sqlite://',
            CAREERS_UPLOAD_ROOT=str(self.root / 'uploads'),
        )
        db.init_app(self.app)
        self.app.register_blueprint(pages_bp)
        self.context = self.app.app_context()
        self.context.push()
        db.create_all()
        for job_id, active in ((1, True), (2, False)):
            db.session.add(JobOpening(
                jobID=job_id, jobTitle=f'Role {job_id}', jobDescription='Test job',
                jobLocation='Office', jobSalary=50000, jobRequirements='Test requirements',
                jobActive=active,
            ))
        db.session.commit()
        self.client = self.app.test_client()
        self.client.get('/careers')
        with self.client.session_transaction() as session:
            self.token = session['careers_csrf']

    def tearDown(self):
        db.session.remove()
        db.engine.dispose()
        self.context.pop()
        self.temp.cleanup()

    def submit(self, **changes):
        data = dict(
            csrf_token=self.token, first_name='Test', last_name='Applicant',
            email='test@example.invalid', phone_number='+1 (555) 123-4567', jobID='1',
            resume=(io.BytesIO(b'%PDF-1.4\nfictional test document'), 'resume.pdf'),
        )
        data.update(changes)
        return self.client.post('/careers', data={k: v for k, v in data.items() if v is not None},
                                content_type='multipart/form-data')

    def files(self):
        return list((self.root / 'uploads').rglob('*.*'))

    def test_get_active_jobs(self):
        response = self.client.get('/careers')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Role 1', response.data)
        self.assertNotIn(b'Role 2', response.data)

    def test_resume_only_saved_and_redirected(self):
        response = self.submit()
        self.assertEqual(response.status_code, 303)
        row = JobApplication.query.one()
        self.assertEqual(row.jobOpening, 1)
        self.assertIsNone(row.cover_letter)
        self.assertIsInstance(row.resume, str)
        self.assertTrue((self.root / 'uploads' / row.resume).is_file())
        self.assertIn(b'submitted successfully', self.client.get(response.location).data)
        self.client.get('/careers')
        self.assertEqual(JobApplication.query.count(), 1)

    def test_both_uploads_saved(self):
        self.assertEqual(self.submit(cover_letter=(io.BytesIO(b'test'), 'cover.docx')).status_code, 303)
        row = JobApplication.query.one()
        self.assertTrue((self.root / 'uploads' / row.cover_letter).is_file())
        self.assertEqual(len(self.files()), 2)

    def test_empty_cover_filename_is_optional(self):
        self.assertEqual(self.submit(cover_letter=(io.BytesIO(b''), '')).status_code, 303)
        self.assertIsNone(JobApplication.query.one().cover_letter)

    def test_missing_or_empty_resume(self):
        for resume in (None, (io.BytesIO(b''), ''), (io.BytesIO(b''), 'empty.pdf')):
            with self.subTest(resume=resume):
                self.assertEqual(self.submit(resume=resume).status_code, 400)
        self.assertEqual(JobApplication.query.count(), 0)

    def test_invalid_jobs(self):
        for job_id in ('', 'abc', '999', '2', '9' * 100, '１２'):
            with self.subTest(job_id=job_id):
                self.assertEqual(self.submit(jobID=job_id).status_code, 400)
        self.assertEqual(JobApplication.query.count(), 0)

    def test_missing_invalid_and_long_fields(self):
        for changes in ({'first_name': ''}, {'last_name': 'x' * 51},
                        {'email': 'not-an-email'}, {'phone_number': 'hello'}):
            with self.subTest(changes=changes):
                self.assertEqual(self.submit(**changes).status_code, 400)

    def test_csrf_required(self):
        for token in (None, 'wrong', '☃'):
            self.assertEqual(self.submit(csrf_token=token).status_code, 400)
        self.assertFalse(self.files())

    def test_bad_file_extensions(self):
        self.assertEqual(self.submit(resume=(io.BytesIO(b'test'), 'resume.exe')).status_code, 400)
        self.assertFalse(self.files())

    def test_untrusted_filename_does_not_control_destination(self):
        self.assertEqual(self.submit(resume=(io.BytesIO(b'test'), '../../resume.pdf')).status_code, 303)
        stored = JobApplication.query.one().resume
        self.assertNotIn('..', stored)
        self.assertNotIn('resume.pdf', stored)

    def test_duplicate_email_does_not_add_files(self):
        self.assertEqual(self.submit().status_code, 303)
        self.assertEqual(self.submit().status_code, 409)
        self.assertEqual(JobApplication.query.count(), 1)
        self.assertEqual(len(self.files()), 1)

    def test_oversized_request(self):
        self.app.config['MAX_CONTENT_LENGTH'] = 2048
        response = self.submit(resume=(io.BytesIO(b'x' * 4096), 'large.pdf'))
        self.assertEqual(response.status_code, 413)
        self.assertIn(b'too large', response.data)
        self.assertFalse(self.files())

    def test_commit_failure_rolls_back_and_removes_uploads(self):
        with patch.object(db.session, 'commit', side_effect=SQLAlchemyError('test failure')):
            response = self.submit(cover_letter=(io.BytesIO(b'test'), 'cover.pdf'))
        self.assertEqual(response.status_code, 500)
        self.assertEqual(JobApplication.query.count(), 0)
        self.assertFalse(self.files())
        self.assertEqual(self.submit().status_code, 303)

    def test_file_failure_is_friendly(self):
        with patch('werkzeug.datastructures.FileStorage.save', side_effect=OSError('test failure')):
            self.assertEqual(self.submit().status_code, 500)
        self.assertFalse(self.files())
        self.assertEqual(JobApplication.query.count(), 0)

    def test_no_jobs_hides_form(self):
        db.session.get(JobOpening, 1).jobActive = False
        db.session.commit()
        response = self.client.get('/careers')
        self.assertIn(b'No active job openings', response.data)
        self.assertNotIn(b'type="submit"', response.data)


class MigrationTests(unittest.TestCase):
    def test_empty_legacy_table_repaired_and_backed_up(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / 'test.db'
            with sqlite3.connect(database) as conn:
                conn.executescript('''
                    CREATE TABLE job_openings (jobID INTEGER PRIMARY KEY);
                    INSERT INTO job_openings VALUES (1);
                    CREATE TABLE job_applications (
                        id INTEGER PRIMARY KEY, first_name TEXT NOT NULL, last_name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE, phone_number TEXT NOT NULL,
                        resume TEXT NOT NULL, cover_letter TEXT);
                ''')
            backup = repair(database)
            self.assertTrue(backup.is_file())
            with sqlite3.connect(database) as conn:
                columns = {r[1]: r for r in conn.execute('PRAGMA table_info(job_applications)')}
                self.assertEqual(columns['jobOpening'][3], 1)
                self.assertEqual(len(conn.execute('PRAGMA foreign_key_list(job_applications)').fetchall()), 1)
                self.assertEqual(conn.execute('SELECT count(*) FROM job_openings').fetchone()[0], 1)
            self.assertIsNone(repair(database))
            with sqlite3.connect(backup) as conn:
                self.assertNotIn('jobOpening', [r[1] for r in conn.execute('PRAGMA table_info(job_applications)')])

    def test_nonempty_legacy_table_is_not_deleted(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / 'test.db'
            with sqlite3.connect(database) as conn:
                conn.executescript('''CREATE TABLE job_applications (
                    id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, email TEXT,
                    phone_number TEXT, resume TEXT, cover_letter TEXT);
                    INSERT INTO job_applications (id) VALUES (1);''')
            with self.assertRaisesRegex(RuntimeError, 'backfill'):
                repair(database)
            with sqlite3.connect(database) as conn:
                self.assertEqual(conn.execute('SELECT count(*) FROM job_applications').fetchone()[0], 1)


if __name__ == '__main__':
    unittest.main()
