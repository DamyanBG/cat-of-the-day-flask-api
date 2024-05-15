from marshmallow import Schema, fields


class ImageRequestSchema(Schema):
    image_base64 = fields.String(required=True)
