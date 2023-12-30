from db import db

from models.enums import RoleType


class BaseUserModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    # phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(255), nullable=False)


class UserModel(BaseUserModel):
    __tablename__ = "users"

# class VoterModel(BaseUserModel):
#     __tablename__ = "voter"

#     role = db.Column(db.Enum(RoleType), default=RoleType.voter, nullable=False)

class AdministratorModel(BaseUserModel):
    __tablename__ = "administrators"
