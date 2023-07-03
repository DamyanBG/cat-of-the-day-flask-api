import base64
import re
import uuid
from mimetypes import guess_extension
from azure.storage.blob import BlobServiceClient
from decouple import config

from db import db
from models.cat_model import CatModel
from models.votes_model import VoteHistoryModel


class CatManager:
    @staticmethod
    def add_cat(cat_data):
        base64_photo = cat_data.pop("photo")
        extension_container, base64_data = base64_photo.split(",")
        photo_bytes = base64.b64decode(base64_data.encode("utf-8"))
        match = re.search(":(.+);", extension_container)
        mime_type = match.group(1)
        file_extension = guess_extension(mime_type)
        file_name = f"{uuid.uuid4()}{file_extension}"
        
        with open(f"photos/{file_name}", "wb") as photo_file:
            photo_file.write(photo_bytes)
        
        cat_data["photo_url"] = f"photos/{file_name}"
        cat = CatModel(**cat_data)
        db.session.add(cat)
        db.session.commit()
        return cat
    
    @staticmethod
    def select_cat_of_user(user_pk):
        cat = CatModel.query.filter_by(uploader_pk=user_pk).first()
        return cat


    @staticmethod
    def select_cat_for_vote(user_pk):
        user_votes_history = VoteHistoryModel.query.filter_by(voter_pk=user_pk).all()
        user_votes_history_cats_pks = [vote_history.cat_pk for vote_history in user_votes_history]
        cat = CatModel.query.filter(CatModel.pk.notin_(user_votes_history_cats_pks)).order_by("votes").first()
        print(cat.photo_url)
        image_file = open(cat.photo_url, "rb")
        image_data_binary = image_file.read()
        image_data = (base64.b64encode(image_data_binary)).decode('ascii')
        print(image_data)
        cat.cat_photo = image_data
        return cat
    
    @staticmethod
    def vote(vote, cat_pk, user_pk):
        vote_history = VoteHistoryModel(cat_pk=cat_pk, voter_pk=user_pk)
        cat = CatModel.query.get(cat_pk)
        cat.votes += 1
        if vote == "like":
            cat.likes += 1
        else:
            cat.dislikes += 1
        db.session.add(vote_history)
        db.session.add(cat)
        db.session.commit()
        print(cat)
        return "OK"
