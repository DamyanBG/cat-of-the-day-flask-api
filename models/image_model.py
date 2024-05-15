from sqlalchemy import func

from db import db


class ImageModel(db.Model):
    __tablename__ = "images"

    pk = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    url = db.Column(db.String(255), nullable=False)
