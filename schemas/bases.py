from marshmallow import Schema, fields, validate


class BaseUserSchema(Schema):
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6, max=255))


class BaseCatSchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=2, max=255))
    passport_id = fields.String(required=True, validate=validate.Length(min=2, max=255))
    microchip_id = fields.String(required=True, validate=validate.Length(min=2, max=255))
    breed = fields.String(validate=validate.Length(max=255))


# class BaseOrderSchema(Schema):
#     title = fields.String(required=True, validate=validate.Length(max=100))
#     description = fields.String(required=True, validate=validate.Length(max=255))
#     address = fields.String(required=True, validate=validate.Length(max=255))
#     color = fields.String(validate=validate.Length(max=255))


# class BaseOfferSchema(Schema):
#     title = fields.String(required=True, validate=validate.Length(max=100))
#     amount = fields.Float(required=True)
#     order_pk = fields.Integer(required=True)


# class BaseProductSchema(Schema):
#     title = fields.String(required=True, validate=validate.Length(max=100))
#     amount = fields.Float(required=True)
#     description = fields.String(required=True, validate=validate.Length(max=255))


# class BaseCartSchema(Schema):
#     quantity = fields.Integer(required=True)


# class BaseCartCloseSchema(Schema):
#     address = fields.String(required=True, validate=validate.Length(max=255))
