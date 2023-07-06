from marshmallow import fields

from schemas.bases import BaseCatSchema


class CatResponseSchema(BaseCatSchema):
    pk = fields.Integer(required=True)
    create_on = fields.DateTime(required=True)
    photo_url = fields.String(required=True)
