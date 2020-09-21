import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'barl'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://balvine:balito20@localhost/pitch'