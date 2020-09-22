from flask import Flask
# from config import config_options 
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    # Creating the app configuration
    
    # app.config.from_object(config_options[config_name])  


    return app