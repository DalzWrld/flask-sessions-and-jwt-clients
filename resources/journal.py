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

class JournalList(Resource):
    @jwt_required()
    def get(self):

        current_user = get_jwt_identity()

        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 5, type=int)

        pagination = (
            JournalEntry.query
            .filter_by(user_id=current_user)
            .order_by(JournalEntry.created_at.desc())
            .paginate(page=page, per_page=per_page)
        )