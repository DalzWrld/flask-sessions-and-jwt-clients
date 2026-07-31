from flask import request, make_response
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource

from models import User, db
from schemas import user_schema


class Register(Resource):
    def post(self):
        data = request.get_json()

        validated_data = register_schema.load(data=data)

        if not username or not email or not password:
            response = {
                "status": 400,
                "message": "Username, email and password are required."
            }
            return make_response(response, 400)

        if User.query.filter_by(username=username).first():
            response = {
                "status": 400,
                "message": "Username already exists."
            }
            return make_response(response, 400)

        if User.query.filter_by(email=email).first():
            response = {
                "status": 400,
                "message": "Email already exists."
            }
            return make_response(response, 400)

        user = User(
            username=username,
            email=email
        )

        user.password = password

        db.session.add(user)
        db.session.commit()

        return user_schema.dump(user), 201
