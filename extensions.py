"""
extensions.py

This module initializes and configures the extensions using flask extensions like SQLAlchemy.
"""

from flask_sqlalchemy import SQLAlchemy

# get the database  from SQLAlchemy instance
db = SQLAlchemy()
