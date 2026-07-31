from marshmallow import Schema, ValidationError, fields, validate, validates_schema


class RegisterSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=True)
    password = fields.Str(load_only=True, validate=validate.Length(min=5))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates_schema
    def validate_schema(self, data, **kwargs):
        errors = {}
        if all(key in data for key in ["first_name", "last_name", "phone"]):
            if len(data["first_name"]) < 1:
                errors["first_name"] = ["Firstname is required"]
            if len(data["last_name"]) < 1:
                errors["last_name"] = ["Lastname is required"]
            if len(data["phone"]) != 10:
                errors["phone"] = ["phone number must be 10 characters"]
        if errors:
            raise ValidationError(errors)

register_schema = RegisterSchema()