from flask import request
from flask_restful import Resource

from managers.auth_manager import auth
from managers.image_manager import ImageManager
from schemas.request.image_request import ImageRequestSchema
from schemas.response.image_response import ImageResponseSchema
from utils.decorators import validate_schema


class ImageResource(Resource):
    @auth.login_required
    @validate_schema(ImageRequestSchema)
    def post(self):
        req_body = request.get_json()
        image = ImageManager.create_image(req_body)
        resp_schema = ImageResponseSchema()
        resp = resp_schema.dump(image), 201
        return resp
