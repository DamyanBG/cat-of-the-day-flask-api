import base64
import re
import uuid
from mimetypes import guess_extension
from azure.storage.blob import BlobServiceClient
from decouple import config

from db import db
from models.cat_model import CatModel


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
        
        # Create the BlobServiceClient object
        connection_string = config('AZ_STORAGE_CONNECTION_STRING')
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client("catphotosdev")
        blob = container_client.upload_blob(name=file_name, data=photo_bytes)
        storage_url = "https://catofthedayphotos.blob.core.windows.net"
        
        cat_data["photo_url"] = f"{storage_url}/catphotosdev/{blob.blob_name}"
        cat = CatModel(**cat_data)
        db.session.add(cat)
        db.session.commit()
        return cat


    @staticmethod
    def select_cat_for_vote():
        cat = CatModel.query.order_by("votes").first()
        return cat
    
    @staticmethod
    def vote(vote, cat_pk):
        cat = CatModel.query.get(cat_pk)
        cat.votes += 1
        if vote == "like":
            cat.likes += 1
        else:
            cat.dislikes += 1
        db.session.add(cat)
        db.session.commit()
        print(cat)
        return "OK"
