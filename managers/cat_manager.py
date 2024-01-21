from werkzeug.exceptions import NotFound

from cloud.nextcloud import upload_base64_image
from db import db
from models.cat_model import CurrentRoundCatsModel, CatOfTheWeekModel, NextRoundCatsModel
from models.votes_model import VoteHistoryModel


class CatManager:
    @staticmethod
    def select_cat_for_vote(user_pk):
        user_votes_history = VoteHistoryModel.query.filter_by(voter_pk=user_pk).all()
        user_votes_history_cats_pks = [
            vote_history.cat_pk for vote_history in user_votes_history
        ]
        cat = (
            CurrentRoundCatsModel.query.filter(CurrentRoundCatsModel.pk.notin_(user_votes_history_cats_pks))
            .order_by("votes")
            .first()
        )
        return cat

    @staticmethod
    def vote(vote, cat_pk, user_pk):
        vote_history = VoteHistoryModel(cat_pk=cat_pk, voter_pk=user_pk)
        cat = CurrentRoundCatsModel.query.get(cat_pk)
        cat.votes += 1
        if vote == "like":
            cat.likes += 1
        else:
            cat.dislikes += 1
        db.session.add(vote_history)
        db.session.add(cat)
        db.session.commit()
        return "OK"

    @staticmethod
    def select_winning_cat():
        winning_cat = db.session.execute(
            db.select(CurrentRoundCatsModel).order_by(db.desc(CurrentRoundCatsModel.likes - CurrentRoundCatsModel.dislikes))
        ).first()
        if not winning_cat:
            return None
        return winning_cat[0]

    @staticmethod
    def reset_votes():
        cats = CurrentRoundCatsModel.query.all()
        for cat in cats:
            cat.votes = 0
            cat.likes = 0
            cat.dislikes = 0

        db.session.commit()

    @staticmethod
    def delete_cats():
        db.session.query(CurrentRoundCatsModel).delete()
        db.session.commit()

    @staticmethod
    def add_cats(cats: list[NextRoundCatsModel]):
        cats_to_add = []
        for cat in cats:
            cats_to_add.append(CurrentRoundCatsModel(
                name=cat.name,
                passport_id=cat.passport_id,
                microchip_id=cat.microchip_id,
                photo_url=cat.photo_url,
                breed=cat.breed,
                user_pk=cat.user_pk,
                user=cat.user,
            ))

        db.session.add_all(cats_to_add)
        db.session.commit()

class CatOfTheDayManager:
    @staticmethod
    def add_cat_of_the_day(cat: CurrentRoundCatsModel):
        cat_of_the_day = CatOfTheWeekModel(
            name=cat.name,
            passport_id=cat.passport_id,
            microchip_id=cat.microchip_id,
            photo_url=cat.photo_url,
            breed=cat.breed,
            user_pk=cat.user_pk,
        )
        db.session.add(cat_of_the_day)
        db.session.commit()

    @staticmethod
    def select_cat_of_the_day_photo():
        cat_of_the_day = CatOfTheWeekModel.query.order_by(db.desc(CatOfTheWeekModel.created_on)).first()
        if not cat_of_the_day:
            raise NotFound("There is no cat of the week!")
        cat_of_the_day_photo = cat_of_the_day.photo_url
        return cat_of_the_day_photo


class NextRoundCatsManager:
    @staticmethod
    def check_has_user_uploaded_cat(cls, user_pk):
        return bool(cls.select_cat_of_user(user_pk))
    
    @staticmethod
    def select_cat_of_user(user_pk):
        cat = NextRoundCatsModel.query.filter_by(user_pk=user_pk).first()
        return cat

    @staticmethod
    def add_cat(cat_data):
        base64_photo = cat_data.pop("photo")
        photo_url = upload_base64_image(base64_photo)
        cat_data["photo_url"] = photo_url
        cat = NextRoundCatsModel(**cat_data)
        db.session.add(cat)
        db.session.commit()
        return cat

    @staticmethod
    def select_all_cats():
        cats = NextRoundCatsModel.query.all()
        return cats
    
    @staticmethod
    def delete_all_cats():
        db.session.query(NextRoundCatsModel).delete()
        db.session.commit()
