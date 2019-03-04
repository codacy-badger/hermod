from flask import Flask, current_app
from hermod.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from hermod.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app

from hermod.quote import models
