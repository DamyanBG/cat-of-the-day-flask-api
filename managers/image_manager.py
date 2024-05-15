from db import db
from models.image_model import ImageModel
from cloud.nextcloud import upload_base64_image

class ImageManager:
    @staticmethod
    def create_image(image_data) -> ImageModel:
        base64_image = image_data.pop("imahe")
        image_url = upload_base64_image(base64_image)
        image = ImageModel(url=image_url)
        db.session.add(image)
        db.session.commit()
        return image

    @staticmethod
    def select_image(image_pk: int) -> ImageModel:
        image = ImageModel.queryfilter_by(user_pk=image_pk).first()
        return image
