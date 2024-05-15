from flask import request
from flask_restful import Resource
from time import sleep

from managers.cat_manager import CatManager
from schemas.response.cat_response import CatResponseSchema
from managers.auth_manager import auth
from managers.image_manager import ImageManager


class Voting(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        cat_for_vote = CatManager.select_cat_for_vote(current_user.pk)
        print(cat_for_vote)
        if not cat_for_vote:
            return {"message": "No more cats for vote!"}, 200
        cat_photo = ImageManager.select_image(cat_for_vote.photo_pk)
        cat_for_vote.photo_url = cat_photo.url
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat_for_vote), 200

    @auth.login_required
    def post(self):
        req_body = request.get_json()
        vote = req_body["vote"]
        cat_pk = req_body["pk"]
        current_user = auth.current_user()
        CatManager.vote(vote, cat_pk, current_user.pk)
        return "OK", 200
