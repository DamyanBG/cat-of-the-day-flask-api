from sqlalchemy import func

from db import db


class CatModel(db.Model):
    __tablename__ = "cats"

    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    passport_id = db.Column(db.String(255), nullable=False)
    microchip_id = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))
    likes = db.Column(db.Integer, default=0)
    dislikes = db.Column(db.Integer, default=0)
    votes = db.Column(db.Integer, default=0)
    uploader_pk = db.Column(db.Integer, db.ForeignKey("uploaders.pk"), unique=True)
    uploader = db.relationship("UploaderModel")


class CatOfTheDayModel(db.Model):
    __tablename__ = "cat_of_the_day"
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    create_on = db.Column(db.DateTime, server_default=func.now())
    # the_day = db.Column(db.DateTime)
    passport_id = db.Column(db.String(255), nullable=False)
    microchip_id = db.Column(db.String(255), nullable=False)
    photo_url = db.Column(db.String(255), nullable=False)
    breed = db.Column(db.String(255))
    uploader_pk = db.Column(db.Integer, db.ForeignKey("uploaders.pk"))
    uploader = db.relationship("UploaderModel")
