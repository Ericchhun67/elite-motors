"""
To seed the seed car inventory database.
date: 2026-09/11


"""


from app import create_app
from extensions import db
from models.car_inventory import CarInventory

from car_data import (
Luxury_cars,
superCars,
sportsCars,
sedanCars,
electricCars,
hybridCars
)


app = create_app()


with app.app_context():
    all_cars = (
    Luxury_cars
    + superCars
    + sportsCars
    + sedanCars
    + electricCars
    + hybridCars
    )

    for car in all_cars:
        existing_car = CarInventory.query.filter_by(
        car_id=car["car_id"]
        ).first()

        if not existing_car:
            new_car = CarInventory(**car)
            db.session.add(new_car)

            db.session.commit()

            print("Cars seeded data successfully added!")
