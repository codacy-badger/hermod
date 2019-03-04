from flask import Blueprint

bp = Blueprint('home', __name__)

from hermod.home import routes
