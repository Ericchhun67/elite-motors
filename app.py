"""
This is the main application file for the Elite Motors web application.
date: 2026-07/17
"""

from flask import Flask, render_template, request, redirect, url_for
from config import Config, developmentConfig
from extensions import db


""" Flask application creates the app object and then stores it in the variable app.
    the __name__ variable is a special python variable that is set to the name of
    the module in which it is used. when the it is run directly
"""
app = Flask(__name__)

app.config.from_object(Config)

app.config.from_object(developmentConfig)

def create_app():
    db.init_app(app)
    
    
    
    
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
