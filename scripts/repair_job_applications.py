"""One-time, backed-up repair for the project's EMPTY legacy application table.

Run from the project root: python3 scripts/repair_job_applications.py
This deliberately refuses to guess job IDs for pre-existing applications.
"""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import sqlite3
from uuid import uuid4


def repair(database):
    database = Path(database).resolve(strict=True)
    with sqlite3.connect(database.as_uri() + '?mode=rw', uri=True) as connection:
        columns = {row[1] for row in connection.execute('PRAGMA table_info(job_applications)')}
        if 'jobOpening' in columns:
            print('jobOpening already exists; no changes made.')
            return None
        expected = {'id', 'first_name', 'last_name', 'email', 'phone_number', 'resume', 'cover_letter'}
        if columns != expected:
            raise RuntimeError('Unexpected schema. Stop and review before migrating.')
        if connection.execute('SELECT COUNT(*) FROM job_applications').fetchone()[0]:
            raise RuntimeError('Applications exist. A reviewed job-ID backfill is required; nothing changed.')
        if connection.execute("SELECT name FROM sqlite_master WHERE tbl_name='job_applications' AND sql IS NOT NULL AND type != 'table'").fetchall():
            raise RuntimeError('Custom indexes/triggers need a reviewed migration; nothing changed.')

        backups = database.parent / 'backups'
        backups.mkdir(exist_ok=True, mode=0o700)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
        backup = backups / f'{database.stem}-before-job-opening-{stamp}-{uuid4().hex[:8]}.db'
        with sqlite3.connect(backup) as target:
            connection.backup(target)
        backup.chmod(0o600)

        # SQLite needs a table rebuild to add this NOT NULL foreign key safely.
        connection.execute('PRAGMA foreign_keys=ON')
        connection.execute('BEGIN IMMEDIATE')
        try:
            # Recheck under the write lock before replacing the empty table.
            if connection.execute('SELECT COUNT(*) FROM job_applications').fetchone()[0]:
                raise RuntimeError('An application was added during migration. Nothing changed.')
            connection.execute('''CREATE TABLE job_applications_repaired (
                id INTEGER NOT NULL PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                email VARCHAR(120) NOT NULL UNIQUE,
                phone_number VARCHAR(20) NOT NULL,
                resume VARCHAR(200) NOT NULL,
                cover_letter TEXT,
                jobOpening INTEGER NOT NULL REFERENCES job_openings(jobID)
            )''')
            connection.execute('DROP TABLE job_applications')
            connection.execute('ALTER TABLE job_applications_repaired RENAME TO job_applications')
            if connection.execute('PRAGMA foreign_key_check').fetchall():
                raise RuntimeError('Foreign-key validation failed; rolling back.')
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        print(f'Repaired empty job_applications table. Backup: {backup}')
        return backup


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--database', type=Path, default=Path(__file__).resolve().parents[1] / 'instance' / 'elite_motors.db')
    repair(parser.parse_args().database)
