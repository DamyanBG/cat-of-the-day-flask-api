from marshmallow import fields, Schema

from schemas.bases import BaseCatSchema


class CatResponseSchema(BaseCatSchema):
    pk = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    photo_url = fields.String(required=True)


class CatOfTheDayPhotoResponseSchema(Schema):
    photo_url = fields.String(required=True)
