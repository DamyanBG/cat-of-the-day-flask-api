from sqlalchemy import func

from db import db


class BaseCatModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    birth_date = db.Column(db.DateTime)
    microchip = db.Column(db.String(255))
    color = db.Column(db.String(255))
    breed = db.Column(db.String(255))


class CurrentRoundCatsModel(BaseCatModel):
    __tablename__ = "current_round_cats"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    votes = db.Column(db.Integer, default=0)
    photo_pk = db.Column(db.Integer, db.ForeignKey("images.pk"), unique=True)
    photo = db.relationship("ImageModel")


class NextRoundCatsModel(BaseCatModel):
    __tablename__ = "next_round_cats"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")
    photo_pk = db.Column(db.Integer, db.ForeignKey("images.pk"), unique=True)
    photo = db.relationship("ImageModel")


class CatOfTheWeekModel(BaseCatModel):
    __tablename__ = "cats_of_the_week"

    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")
    photo_pk = db.Column(db.Integer, db.ForeignKey("images.pk"), unique=True)
    photo = db.relationship("ImageModel")

    # the_day = db.Column(db.DateTime)
