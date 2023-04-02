from flask import request
from flask_restful import Resource

from managers.auth_manager import AuthManager
from managers.user_manager import UserManager
from schemas.request.user_request import (
    VoterLoginRequestSchema,
    VoterRegisterRequestSchema,
    UploaderLoginRequestSchema,
    UploaderRegisterRequestSchema,
    AdminLoginRequestSchema,
)
from utils.decorators import validate_schema


class RegisterVoter(Resource):
    @validate_schema(VoterRegisterRequestSchema)
    def post(self):
        print("trigger")
        user = UserManager.register_voter(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class LoginVoter(Resource):
    @validate_schema(VoterLoginRequestSchema)
    def post(self):
        request_body = request.get_json()
        print(request_body)
        user = UserManager.login_voter(request_body)
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class RegisterUploader(Resource):
    @validate_schema(UploaderRegisterRequestSchema)
    def post(self):
        user = UserManager.register_uploader(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 201


class LoginUploader(Resource):
    @validate_schema(UploaderLoginRequestSchema)
    def post(self):
        user = UserManager.login_uploader(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "user_pk": user.pk}, 200


class LoginAdmin(Resource):
    @validate_schema(AdminLoginRequestSchema)
    def post(self):
        user = UserManager.login_admin(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200
