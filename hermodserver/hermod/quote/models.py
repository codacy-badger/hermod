from hermod.app import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(150),index=True)
    body = db.Column(db.Text)

    def __repr__(self):
        return '<Author {}>'.format(self.author)
