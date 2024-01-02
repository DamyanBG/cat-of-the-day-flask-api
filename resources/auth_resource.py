from flask import request
from flask_restful import Resource

from managers.auth_manager import AuthManager, auth
from managers.user_manager import UserManager
from managers.cat_manager import NextRoundCatsManager, CatManager
from schemas.request.user_request import (
    UserLoginRequestSchema,
    UserRegisterRequestSchema,
    AdminLoginRequestSchema,
)
from schemas.response.user_response import BaseUserResponseSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        user = UserManager.register_user(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token, "user_pk": user.pk}, 201


class LoginUser(Resource):
    @validate_schema(UserLoginRequestSchema)
    def post(self):
        user = UserManager.login_user(request.get_json())
        has_uploaded_cat = NextRoundCatsManager.check_has_user_uploaded_cat(user.pk)
        print(has_uploaded_cat)
        token = AuthManager.encode_token(user)
        return {
            "token": token,
            "user_pk": user.pk,
            "has_uploaded_cat": has_uploaded_cat,
        }, 200


class LoginAdmin(Resource):
    @validate_schema(AdminLoginRequestSchema)
    def post(self):
        user = UserManager.login_admin(request.get_json())
        token = AuthManager.encode_token(user)
        return {"token": token}, 200


class UserInfo(Resource):
    @auth.login_required
    def get(self):
        current_user = auth.current_user()
        del current_user.password
        user_schema = BaseUserResponseSchema()
        return user_schema.dump(current_user)
    
    @auth.login_required
    def delete(self):
        current_user = auth.current_user()
        NextRoundCatsManager.delete_user_cat(current_user.pk)
        CatManager.delete_user_cat(current_user.pk)
        UserManager.delete_user(current_user.pk)
        return "OK", 204


class Logout(Resource):
    @auth.login_required
    def post(self):
        req_body = request.get_json()
        token = req_body["token"]
        AuthManager.black_list_token(token)
        return "OK", 201
