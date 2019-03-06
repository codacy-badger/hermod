# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify
from marshmallow import fields

from .models import Quote
from .schemas import (quote_schema, quotes_schema)

blueprint = Blueprint('quote', __name__)

@blueprint.route('/api/quotes', methods=('GET',))
def get_quotes():
    all_quotes = Quote.query.all()
    result = quotes_schema.dump(all_quotes)
    return jsonify(result.data)
