from marshmallow import Schema, fields


class ImageResponseSchema(Schema):
    pk = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    url = fields.String(required=True)
    