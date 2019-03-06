# -*- coding: utf-8 -*-

from hermod.database import db, Column, Model,SurrogatePK

class Quote(SurrogatePK,Model):
    author = Column(db.String(150),index=True)
    body = Column(db.Text)

    def __repr__(self):
        return '<Author {}>'.format(self.author)
