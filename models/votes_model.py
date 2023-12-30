from sqlalchemy import func

from db import db


class VoteHistoryModel(db.Model):
    __tablename__ = "votes_history"

    pk = db.Column(db.Integer, primary_key=True)
    voter_pk = db.Column(db.Integer, db.ForeignKey("users.pk"))
    voter = db.relationship("UserModel")
    cat_pk = db.Column(db.Integer, db.ForeignKey("cats.pk"))
    cat = db.relationship("CatModel")
