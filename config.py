""" the settings for the app """


class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///elite_motors.db'
    

class developmentConfig(Config):
    # Development-specific configuration settings
    DEBUG = True # Enable debug mode for development, provides detailed error pages 
    # and auto-reloading of the server on code changes
