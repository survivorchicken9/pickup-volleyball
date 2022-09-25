from common.database import Database


def insert_to_games():
    test_games = {
        "date": "2022-02-02",  # year month day
        "start_time": "12:00",
        "end_time": "14:00",
        "location": "sports hall 2",
        "notes": "be there please"
    }

    Database.insert_one(test_games)
