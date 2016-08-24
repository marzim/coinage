__author__ = 'marzim'
import os
# default configuration

DEBUG = False
SECRET_KEY = os.environ['MYSECRETKEY']
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
# class BaseConfig(object):
#     DEBUG = False
#     SECRET_KEY = os.environ['MYSECRETKEY']
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#
# class DevelopmentConfig(BaseConfig):
#     DEBUG = True
#
# class ProductionConfig(BaseConfig):
#     DEBUG = False
