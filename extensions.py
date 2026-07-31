from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from structlog import get_logger

bcrypt = Bcrypt()
jwt = JWTManager()

log = get_logger()
