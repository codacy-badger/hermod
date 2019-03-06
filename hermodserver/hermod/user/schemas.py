# -*- coding: utf-8 -*-
from marshmallow import Schema, fields, pre_load, post_dump
from hermod.database import ModelSchema
from .models import *

class UserSchema(ModelSchema):
    class Meta:
        model = User
        # Fields to expose
        fields = ('username', 'email')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
