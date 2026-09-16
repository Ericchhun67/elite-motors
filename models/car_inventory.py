""" car inventory.py 
This model represents the car inventory in the Elite Motors dealership.
This model defines the structure of the car inventory table in the database, that 
has columns for the name ID, car description, year, model, price, color, availability, 
and image file of the car.
"""


from extensions import db



class CarInventory(db.Model):
    """Car inventory model for Elite Motors dealership. db.Models represents a 
    table in the database."""
    __tablename__ = 'car_inventory'
    car_id = db.Column(db.Integer, primary_key=True) # Unique ID for each car in the inventory
    # get the python attribute names for the columns in the table and the 
    # corresponding database column names
    car_name = db.Column(db.String(300), nullable=False) 
    car_description = db.Column(db.String(1000), nullable=False) # car_description of the car
    year =  db.Column(db.Integer, nullable=False) # year of the car
    model = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True, nullable=False)
    imagefile = db.Column(db.String(250), nullable=True)
    
    def __repr__(self):
        # return name, car_description, year, model, price, imagefile to string because 
        # it is a representation of the object
        return f"CarInventory(id={self.car_id}, name='{self.car_name}', \
            car_description='{self.car_description}', year={self.year}, \
            model='{self.model}', price={self.price}, availability={self.availability}, \
            imagefile='{self.imagefile}')"