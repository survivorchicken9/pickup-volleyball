from common.database import Database


def insert_to_teams():
    test_team_1 = {
        "game_id": "633045b5c6fc407490585935",
        "outside_hitter_1": "Byron",
        "outside_hitter_2": "Chris",
        "middle_blocker_1": "Max",
        "middle_blocker_2": "Li",
        "setter": "No",
        "opposite_hitter": "Me",
    }
    test_team_2 = {
        "game_id": "633045b5c6fc407490585935",
        "outside_hitter_1": "F",
        "outside_hitter_2": "ChrDis",
        "middle_blocker_1": "D",
        "middle_blocker_2": "fesq",
        "setter": "Fd",
        "opposite_hitter": "Fjklfda",
    }

    Database.insert_one(collection="teams", data=test_team_1)
    print("inserted 1")
    Database.insert_one(collection="teams", data=test_team_2)
    print("inserted 2")
