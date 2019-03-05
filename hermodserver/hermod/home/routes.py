from flask import Blueprint

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
@blueprint.route('/index')
def index():
    return "Hello, World!"
