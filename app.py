import os

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from extensions import bcrypt, jwt, log
from models import db
from resources.auth import LoggedIn, Login, Logout, Register
from resources.journal import Journal, JournalList

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "sqlite:///instance/app.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

CORS(app)

migrate = Migrate(app, db)
api = Api(app)



api.add_resource(Register, "/register")
api.add_resource(Login, "/login")
api.add_resource(Logout, "/logout")
api.add_resource(LoggedIn, "/loggedin")

api.add_resource(JournalList, "/journal")
api.add_resource(Journal, "/journal/<int:id>")

@app.before_request
def log_request():
    log.info(
        "request",
        method=request.method,
        content_type=request.headers.get("Content-Type"),
    )

@app.route("/")
def home():
    return {
        "message": "Journal API is running!"
    }


if __name__ == "__main__":
    app.run(debug=True)