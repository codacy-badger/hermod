from hermod.database import db, Column, Model

class Quote(Model):
    id = Column(db.Integer, primary_key = True)
    author = Column(db.String(150),index=True)
    body = Column(db.Text)

    def __repr__(self):
        return '<Author {}>'.format(self.author)
