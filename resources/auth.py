from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required
)

from models import db, User
from schemas import user_schema

class Register(Resource):
    