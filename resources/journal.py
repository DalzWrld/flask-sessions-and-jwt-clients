from flask import request
from flask_restful import Resource
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from models import db, JournalEntry
from schemas import (
    journal_schema,
    journals_schema
)