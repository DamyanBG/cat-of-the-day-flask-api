from models.votes_model import VoteHistoryModel
from db import db

class VoteHistoryManager:
    @staticmethod
    def delete_all_history():
        vote_histories = VoteHistoryModel.query.all()
        for vh in vote_histories:
            db.session.delete(vh)
        db.session.commit()
