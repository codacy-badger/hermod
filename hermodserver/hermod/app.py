# -*- coding: utf-8 -*-
from flask import Flask, current_app

from hermod import home, quote, user
from hermod.config import Config
from hermod.extensions import db, migrate, ma, bcrypt, jwt

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.routes.blueprint)
    app.register_blueprint(quote.routes.blueprint)
    app.register_blueprint(user.routes.blueprint)
