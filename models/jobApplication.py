""" 
This module defines the JobApplication model for the Elite Motors web application.
it represents a job application submitted by a user, including details such as the 
first name, last name, email, phone number, uploading resume, and cover letter.

"""
from extensions import db

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    phone_number = db.Column(db.String(20), nullable=False)
    # path to uploaded resume file and cover letter file if any
    resume = db.Column(db.String(200), nullable=False)
    cover_letter = db.Column(db.Text, nullable=True)
    jobOpening = db.Column(db.Integer, db.ForeignKey('job_openings.jobID'), nullable=False)

    def __repr__(self):
        return f"job_application<{self.id} {self.first_name} {self.last_name} \
        {self.email} {self.phone_number} {self.resume} {self.cover_letter} {self.jobOpening}>"