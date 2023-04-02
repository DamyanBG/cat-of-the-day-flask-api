from db import db
from models.cat_model import CatModel


class CatManager:
    @staticmethod
    def add_cat(cat_data):
        cat = CatModel(**cat_data)
        db.session.add(cat)
        db.session.commit()
        return cat
