# -*- coding: utf-8 -*-  
from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_pagedown import PageDown

pagedown = PageDown()
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    pagedown.init_app(app)
    configure_uploads(app,photos)
    patch_request_class(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app