# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""

from .extensions import db, ma

# Alias common SQLAlchemy names
Column = db.Column
Model = db.Model

# Alias commom for Marshmallow schemas
ModelSchema = ma.ModelSchema
