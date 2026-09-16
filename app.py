"""
This is the main application file for the Elite Motors web application.
date: 2026-07/17
"""

from flask import Flask, render_template, request, redirect, url_for
from config import Config, developmentConfig
from extensions import db
from routes.pages import pages_bp as pages_bp


""" Flask application creates the app object and then stores it in the variable app.
the __name__ variable is a special python variable that is set to the name of
the module in which it is used. when the it is run directly
"""
app = Flask(__name__)


app.config.from_object(Config)

app.config.from_object(developmentConfig)


def create_app():
    db.init_app(app)  # Initialize the database with the Flask ap
    # Blueprints for different routes and functionalities can be registered here if needed
    # here.
    app.register_blueprint(pages_bp)  # Register the pages blueprint for handling routes related to pages

    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy before creating tables
        from models.car_inventory import CarInventory
        

        db.create_all()  # Create database tables based on the defined models

    return app  # Return the initialized Flask application instance


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
