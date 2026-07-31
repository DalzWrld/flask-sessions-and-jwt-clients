from marshmallow import Schema, fields


class JournalEntrySchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    user = fields.Nested("UserSchema", only=("id", "username", "email"))

journal_schema = JournalEntrySchema()
journals_schema = JournalEntrySchema(many=True)