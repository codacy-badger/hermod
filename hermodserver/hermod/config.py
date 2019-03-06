# -*- coding: utf-8 -*-
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'hermod.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 13
    JWT_SECRET_KEY = 'jwt-secret-string'

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4

class DevConfig(Config):
    ENV = 'dev'
    DEBUG = True

class ProdConfig(Config):
    ENV = 'prod'
    DEBUG = False
