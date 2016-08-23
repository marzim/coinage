__author__ = 'Marvin'
import os
# default configuration

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = os.environ['MYSECRETKEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
