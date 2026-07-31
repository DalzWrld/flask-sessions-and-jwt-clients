from flask import make_response, request, session
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_restful import Resource

from models.user import User, db
from schemas import user_schema


class Register(Resource):
    def post(self):
        data = request.get_json(force=True)
    
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
    
        if not username or not email or not password:
            return {
                "message": "Username, email and password are required."
            }, 400
    
        if User.query.filter_by(username=username).first():
            return {
                "message": "Username already exists."
            }, 400
    
        if User.query.filter_by(email=email).first():
            return {
                "message": "Email already exists."
            }, 400
    
        user = User(
            username=username,
            email=email
        )
    
        user.password = password
    
        db.session.add(user)
        db.session.commit()
    
        return make_response(user_schema.dump(user), 201)


class Login(Resource):
    def post(self):
        data = request.get_json(force=True)

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