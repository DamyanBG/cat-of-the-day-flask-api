from managers.cat_manager import CatManager, CatOfTheDayManager, NextRoundCatsManager
from managers.votes_history_manager import VoteHistoryManager


def won(app):
    def execute():
        with app.app_context():
            print("trigger won cron job")
            winning_cat = CatManager.select_winning_cat()
            if winning_cat:
                CatOfTheDayManager.add_cat_of_the_day(winning_cat)
            VoteHistoryManager.delete_all_history()
            CatManager.delete_cats()
            new_round_cats = NextRoundCatsManager.select_all_cats()
            CatManager.add_cats(new_round_cats)
            NextRoundCatsManager.delete_all_cats()

    return execute


def test(app):
    def execute():
        with app.app_context():
            print("Running")

    return execute
