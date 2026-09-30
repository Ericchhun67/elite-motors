""" 
jobopening model
Add jobID field to the job opening model.
add title field to the job opening model.
add description field to the job opening model.
add location field to the job opening model.
add salary field to the job opening model.
add requirements field to the job opening model.
add whether this job opening is active.

"""

from extensions import db

class JobOpening(db.Model):
    __tablename__ = 'job_openings'
    jobID = db.Column(db.Integer, primary_key=True)
    jobTitle = db.Column(db.String(255), nullable=False)
    jobDescription = db.Column(db.Text, nullable=False)
    jobLocation = db.Column(db.String(255), nullable=False)
    jobSalary = db.Column(db.Float, nullable=False)
    jobRequirements = db.Column(db.Text, nullable=False)
    jobActive = db.Column(db.Boolean, default=True, nullable=False)
    
    def __repr__(self):
        return f"<JobOpening(jobID={self.jobID}, jobTitle={self.jobTitle}, \
        jobDescription={self.jobDescription}, \
        jobLocation={self.jobLocation}, jobSalary={self.jobSalary}, \
        jobRequirements={self.jobRequirements}, jobActive={self.jobActive})>"
    