from flask import make_response, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from models import JournalEntry, db
from schemas import journal_schema, journals_schema


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

        return make_response({
            "entries": journals_schema.dump(pagination.items),
            "page": pagination.page,
            "pages": pagination.pages,
            "total": pagination.total
        }, 200)

    @jwt_required()
    def post(self):

        current_user = get_jwt_identity()

        data = request.get_json()

        title = data.get("title")
        content = data.get("content")

        if not title or not content:
            response = {
                "status": 400,
                "message": "Title and content are required."
            }
            return make_response(response, 400)

        entry = JournalEntry(
            title=title,
            content=content,
            user_id=current_user
        )

        db.session.add(entry)
        db.session.commit()

        return make_response(journal_schema.dump(entry), 201)