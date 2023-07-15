from flask import request
from flask_restful import Resource

from utils.decorators import validate_schema
from schemas.request.cat_request import CatRequestSchema
from schemas.response.cat_response import CatResponseSchema, CatOfTheDayPhotoResponseSchema
from managers.cat_manager import CatManager, CatOfTheDayManager
from managers.auth_manager import auth


class AddCat(Resource):
    @validate_schema(CatRequestSchema)
    def post(self):
        req_body = request.get_json()
        cat = CatManager.add_cat(req_body)
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat)

    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        print(current_user)
        cat_of_user = CatManager.select_cat_of_user(current_user.pk)
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat_of_user)
    

class GetCatOfTheDayPhoto(Resource):
    def get(self):
        cat_of_the_day_photo = CatOfTheDayManager.select_cat_of_the_day_photo()
        return cat_of_the_day_photo, 200
