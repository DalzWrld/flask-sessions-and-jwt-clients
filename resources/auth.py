from flask import make_response, request, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource
from marshmallow import IntegrityError, ValidationError

from extensions import log
from models.user import User, db
from schemas import register_schema, user_schema


class Register(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = register_schema.load(data=data)
            
            if User.query.filter_by(email=validated_data["email"]).first():
                return make_response(
                    {"status": 409, "message": "Email address already taken"}, 409
                )
            if User.query.filter_by(username=validated_data["username"]).first():
                return make_response(
                    {"status": 409, "message": "Username already taken"}, 409
                )
                    
            user = User(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )
                    
            user.set_password(validated_data["password"])
            
            db.session.add(user)
            db.session.commit()
            
            session["user_id"] = user.id
            
            response = {
                "message": "Account created successfully",
                "data": user_schema.dump(user)
            }
            return make_response(response, 200)

        except ValidationError as err:
            log.error("validation_error", errors=err.messages)
            response = {
                "status": 400,
                "message": "Validation error(s) occurred",
                "errors": {**err.messages},
            }
            return make_response(response, 400)

        except IntegrityError as ie:
            db.session.rollback()
            log.error(
                "integrity_error", error=str(ie)
            )
            response = {
                "status": 409,
                "message": "A user with that email address or phone already exists",
            }
        
            return make_response(response, 409)

        except Exception as e:  # noqa: BLE001
            db.session.rollback()
            log.error("unexpected_error", error=str(e))
            response = {
                "status": 500,
                "message": "An internal server error occurred",
            }
            return make_response(response, 500)


class Login(Resource):
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        user = User.query.filter_by(email=email).first()

        if not user or not user.authenticate(password):
            response = {
                "status": 401,
                "message": "Invalid email or password."
            }
            return make_response(response, 401)

        access_token = create_access_token(identity=user.id)

        return make_response({
            "access_token": access_token,
            "user": user_schema.dump(user)
        }, 200)


class LoggedIn(Resource):
    @jwt_required()
    def get(self):

        current_user = get_jwt_identity()

        user = User.query.get(current_user)

        if not user:
            response = {
                "status": 404,
                "message": "User not found."
            }
            return make_response(response, 404)

        return make_response(user_schema.dump(user), 200)


class Logout(Resource):
    def delete(self):
        session.clear()
        return {}, 204