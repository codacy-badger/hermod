from hermod.app import create_app, db
import hermod.cli as cli

# Import models
from hermod.quote.models import *

app = create_app()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Quote': Quote}
