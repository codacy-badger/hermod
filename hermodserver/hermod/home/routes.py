from hermod.home import bp

@bp.route('/')
@bp.route('/index')
def index():
    return "Hello, World!"
