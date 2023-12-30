from sqlalchemy import func

from db import db


class CatModel(db.Model):
    __tablename__ = "cats"

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    passport_id = db.Column(db.String(255))
    microchip_id = db.Column(db.String(255))
    photo_url = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    votes = db.Column(db.Integer, default=0)
    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"), unique=True)
    user = db.relationship("UserModel")


class CatOfTheWeekModel(db.Model):
    __tablename__ = "cats_of_the_week"
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    # the_day = db.Column(db.DateTime)
    passport_id = db.Column(db.String(255), nullable=False)
    microchip_id = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))
    user_pk = db.Column(db.Integer, db.ForeignKey("users.pk"))
    user = db.relationship("UploaderModel")
