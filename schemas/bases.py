from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class BaseCatSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    microchip = fields.String(required=True, validate=validate.Length(min=2, max=255))
    breed = fields.String(required=True, validate=validate.Length(max=255))
    color = fields.String(required=True, validate=validate.Length(max=255))
    birth_date = fields.String(required=True, validate=validate.Length(max=100))
