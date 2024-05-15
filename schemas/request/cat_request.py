from marshmallow import fields, validate

from schemas.bases import BaseCatSchema


class CatRequestSchema(BaseCatSchema):
    photo_pk = fields.String(required=True)
