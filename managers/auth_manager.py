from datetime import datetime, timedelta

import jwt
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import BadRequest

# from models.user_models import AdministratorModel, UserModel

# mapper = {
#     AdministratorModel: lambda: AdministratorModel.query.filter_by(id=x),
#     UserModel: lambda: UserModel.query.filter_by(id=x),
# }


black_listed_tokens = set()


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {
            "sub": user.pk,
            "exp": datetime.utcnow() + timedelta(days=1),
            "role": user.__class__.__name__,
        }
        return jwt.encode(payload, key=config("JWT_KEY"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        if token in black_listed_tokens:
            raise BadRequest("Invalid token")
        try:
            data = jwt.decode(token, key=config("JWT_KEY"), algorithms=["HS256"])
            return data["sub"], data["role"]
        except jwt.ExpiredSignatureError:
            raise BadRequest("Token expired")
        except jwt.InvalidTokenError:
            raise BadRequest("Invalid token")
        
    @staticmethod
    def black_list_token(token):
        black_listed_tokens.add(token)


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    user_pk, role = AuthManager.decode_token(token)
    # user = mapper[role](user_pk)
    user = eval(f"{role}.query.filter_by(pk={user_pk}).first()")
    return user
