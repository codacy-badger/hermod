# -*- coding: utf-8 -*-
from flask import request, Blueprint, jsonify
from flask_apispec import use_kwargs, marshal_with
from marshmallow import fields

from .models import User
from .schemas import (user_schema, users_schema)
from hermod.shared.response import custom_response 

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

blueprint = Blueprint('user', __name__)

@blueprint.route('/api/users', methods=('GET',))
@jwt_required
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)

@blueprint.route('/api/users/create', methods=('POST',))
@jwt_required
def create_user():
    req_data = request.get_json()
    password = request.json.get('password')
    data, error = user_schema.load(req_data)

    if error:
        return custom_response(error, 400)

    # check if user already exist in the db
    user_in_db = User.get_user_by_email(data.email)

    if user_in_db:
        message = {'error': 'User already exist, please supply another email address'}
        return custom_response(message, 400)

    user = User(data.username,data.email,password)
    user.save()
    ser_data = user_schema.dump(user).data

    access_token = create_access_token(ser_data.get('username'))
    refresh_token = create_refresh_token(ser_data.get('username'))

    return custom_response({
        'access_token': access_token,
        'refresh_token': refresh_token,
        }, 201)

@blueprint.route('/api/users/login', methods=('POST',))
def login_user():
    username = request.json.get('username')
    password = request.json.get('password')

    current_user = User.get_user_by_username(username)

    if not current_user:
        message = {'message': 'User {} doesn\'t exist'.format(username)}
        return custom_response(message, 500)

    if current_user.check_password(password):
        access_token = create_access_token(username)
        refresh_token = create_refresh_token(username)
        return custom_response({
            'access_token': access_token,
            'refresh_token': refresh_token,
            }, 201)
    else:
        message = {'message': 'Wrong credentials'}
        return custom_response(message, 500)
