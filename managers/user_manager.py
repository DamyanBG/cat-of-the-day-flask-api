from psycopg2.errorcodes import UNIQUE_VIOLATION
from werkzeug.exceptions import BadRequest, InternalServerError
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from models.user_models import UserModel, AdministratorModel


class UserManager:
    @staticmethod
    def register_user(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = UserModel(**user_data)
        db.session.add(user)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                # To find better error description, this is database error, not back end sever error
                InternalServerError("Server error")
        return user

    @staticmethod
    def login_user(user_data):
        user = UserModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def login_admin(user_data):
        user = AdministratorModel.query.filter_by(email=user_data["email"]).first()
        if not user:
            raise BadRequest("Wrong email or password")

        if not check_password_hash(user.password, user_data["password"]):
            raise BadRequest("Wrong email or password")

        return user

    @staticmethod
    def create_admin(data):
        data["password"] = generate_password_hash(data["password"])
        admin = AdministratorModel(**data)
        db.session.add(admin)
        try:
            db.session.commit()
        except Exception as ex:
            if ex.orig.pgcode == UNIQUE_VIOLATION:
                raise BadRequest("Please login")
            else:
                InternalServerError("Server error")
        return admin


    @staticmethod
    def delete_user(user_pk):
        user = UserModel.query.filter_by(pk=user_pk).first()

        db.session.delete(user)
        db.session.commit()