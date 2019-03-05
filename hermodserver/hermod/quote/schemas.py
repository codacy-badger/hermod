# coding: utf-8

from marshmallow import Schema, fields, pre_load, post_dump
from hermod.database import ModelSchema
from .models import *

class QuoteSchema(ModelSchema):
    class Meta:
        model = Quote
        # Fields to expose
        fields = ('body', 'author')

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)
