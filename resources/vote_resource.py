from flask import request
from flask_restful import Resource

from managers.cat_manager import CatManager
from schemas.response.cat_response import CatResponseSchema


class Voting(Resource):
    def get(self):
        cat_for_vote = CatManager.select_cat_for_vote()
        resp_schema = CatResponseSchema()
        return resp_schema.dump(cat_for_vote)
    
    def post(self):
        req_body = request.get_json()
        vote = req_body["vote"]
        cat_pk = req_body["pk"]
        CatManager.vote(vote, cat_pk)
        return "OK"