from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)

    journal_entries = fields.Nested("JournalEntrySchema", many=True, exclude=("user",))

user_schema = UserSchema()
users_schema = UserSchema(many=True)