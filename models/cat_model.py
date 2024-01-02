from sqlalchemy import func

from db import db


class BaseCatModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    passport_id = db.Column(db.String(255))
    microchip_id = db.Column(db.String(255))
    photo_url = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))


class CurrentRoundCatsModel(BaseCatModel):
    __tablename__ = "current_round_cats"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    votes = db.Column(db.Integer, default=0)


class NextRoundCatsModel(BaseCatModel):
    __tablename__ = "next_round_cats"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")


class CatOfTheWeekModel(BaseCatModel):
    __tablename__ = "cats_of_the_week"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")

    # the_day = db.Column(db.DateTime)
