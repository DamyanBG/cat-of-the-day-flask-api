from managers.cat_manager import CatManager, CatOfTheDayManager
from managers.votes_history_manager import VoteHistoryManager


def won(app):
    def execute():
        with app.app_context():
            print("tigger")
            winning_cat = CatManager.select_winning_cat()
            CatOfTheDayManager.add_cat_of_the_day(winning_cat)
            CatManager.reset_votes()
            VoteHistoryManager.delete_all_history()

    return execute
