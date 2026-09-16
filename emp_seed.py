""" 
To seed the employee database with initial data.
date: 2026-09-13
"""


from app import create_app
from extensions import db
from models.employee import Employee
from datetime import date


from Employee_data import (
    management_employees,
    sale_team,
    Enginnering_team,
    design_team,
    marketing_team
)


app = create_app()


with app.app_context():
    all_employees = (
        management_employees
        + sale_team
        + Enginnering_team
        + design_team
        + marketing_team
    )
    # get all emplpyees staff from the combine list of all employee groups
    for emp_data in all_employees:
        existing_employee = Employee.query.filter_by(
        employee_id=emp_data["employee_id"]
        ).first()
        
        
        if not existing_employee:
            new_employee = Employee(**emp_data)
            db.session.add(new_employee)
            
            
            db.session.commit()
    
     # add a loading bar that would simulate the seeding process and 
     # print print("Employee database seeded successfully loaded.")
    error_occurred = False # Flag to indicate if an error occurred during seeding
    if error_occurred: # check if an error occurred, then print error message
        print("An error occurred during the seeding process.")
        exit(1) # exit with error code
    else:
        # loop to simulate loading progress
        for i in range(0, 101, 10):
            # simulate some processing time for each step of the loading bar
            print(f"loading... {i}%")
            import time 
            time.sleep(0.1) # simulate a short delay for each step of the loading bar
        # indicate that the loading process is complete
        print("Employee database seeded successfully loaded.")