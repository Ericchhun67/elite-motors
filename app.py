"""
This is the main application file for the Elite Motors web application.
"""

from flask import Flask, render_template, request, redirect, url_for
from config import Config, developmentConfig
from extensions import db

app = Flask(__name__) # Initialize the Flask application
app.config.from_object(Config)

app.config.from_object(developmentConfig)

def create_app():
    db.init_app(app)
    
    
    
    
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
