# -*- coding: utf-8 -*-
from flask import request,Blueprint, jsonify
from marshmallow import fields

from .models import Quote
from .schemas import (quote_schema, quotes_schema)

from flask_jwt_extended import (jwt_required)

from hermod.shared.response import custom_response

blueprint = Blueprint('quote', __name__)

@blueprint.route('/api/quotes', methods=('GET',))
def get_quotes():
    all_quotes = Quote.query.all()
    result = quotes_schema.dump(all_quotes)
    return jsonify(result.data)

@blueprint.route('/api/quotes/create', methods=('POST',))
@jwt_required
def create_quote():
    body = request.json.get('body')
    author = request.json.get('author')

    quote = Quote(body = body, author = author)
    quote.save()
    return custom_response({'message':'quote created'}, 301)
