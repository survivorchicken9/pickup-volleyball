from common.database import Database


def insert_to_players():
    test = {
        "game_id": 1,
        "name": "Chris",
        "pos1": "Outside Hitter",
        "pos2": "Middle Blocker",
        "pos3": "Setter"
    }
    Database.insert_one(collection="players", data=test)
