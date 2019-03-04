from hermod.app import app, db

# Import models
from hermod.quote.models import *

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Quote': Quote}
