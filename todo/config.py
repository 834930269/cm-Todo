# -*- coding: utf-8 -*-  
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KET') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = os.path.abspath(os.path.join(os.getcwd(),"app/static/Gravatar"))

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://'+os.environ.get('DATABASE_USERNAME')+':'+os.environ.get('DATABASE_PASSWORD')+'@localhost/notebook'

config={
    'default' : DevelopmentConfig 
}