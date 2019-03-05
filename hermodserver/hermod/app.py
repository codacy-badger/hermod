from flask import Flask, current_app

from hermod import home, quote
from hermod.config import Config
from hermod.extensions import db, migrate, ma

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)
    register_blueprints(app)

    return app

def register_extensions(app):
    """Register Flask extensions."""
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(home.routes.blueprint)
    app.register_blueprint(quote.routes.blueprint)
