""" 
To seed the job opening database with initial data

"""


from app import create_app
from extensions import db
from models.jobopening import JobOpening
from job_opening_database import (
    management_opening,
    sale_team,
    Enginnering_team
)


app = create_app()



with app.app_context():
    all_openings = (
        management_opening
        + sale_team
        + Enginnering_team
    )
    
    
    for opening_data in all_openings:
        existing_opening = JobOpening.query.filter_by(
            jobID=opening_data['jobID'] # store the jobID from the database 
        ).first()
        
        
        if not existing_opening:
            new_opening = JobOpening(**opening_data)
            db.session.add(new_opening)
            
            db.session.commit()
        
    error_occurred = False
        
    if error_occurred:
        print("Error occurred while processing job opening.")
        exit(1)
    else:
        for i in range(0, 101, 10):
            print(f"loading.......... {i}%")
            import time
            time.sleep(0.5)
            
        print("job opening processed successfully.")

