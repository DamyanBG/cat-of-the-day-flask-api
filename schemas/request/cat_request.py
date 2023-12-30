from marshmallow import fields, validate

from schemas.bases import BaseCatSchema


class CatRequestSchema(BaseCatSchema):
    photo = fields.String(required=True)
