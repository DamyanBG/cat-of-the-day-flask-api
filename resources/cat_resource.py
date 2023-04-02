from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from schemas.request.cat_request import CatRequestSchema
from managers.cat_manager import CatManager


class AddCat(Resource):
    @validate_schema(CatRequestSchema)
    def post(self):
        req_body = request.get_json()
        print(req_body)
        # cat = CatManager(req_body)
        return "OK"