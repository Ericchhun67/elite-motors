""" 
employee.py
Defines the Employee model for the database.
This model includes fields for employee_id, first_name, last_name, hire_date, 
position, department, and bio.
"""

from extensions import db




class Employee(db.Model):
    __tablename__ = 'employees'
    
    employee_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    position = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    imagefile = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return f"<Employee (Employee_id: {self.employee_id}): {self.first_name} \
        {self.last_name} {self.hire_date} {self.position} {self.department} {self.bio} \
            imagefile: {self.imagefile}>"


