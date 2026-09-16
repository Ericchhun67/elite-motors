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
    
    