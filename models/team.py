import uuid
from common.database import Database
from dataclasses import dataclass, field


@dataclass(eq=False)
class Team:
    collection: str = field(init=False, default="players")
    game_id: str
    outside_hitter_1: str
    outside_hitter_2: str
    middle_blocker_1: str
    middle_blocker_2: str
    opposite_hitter: str
    setter: str
    libero: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> dict:
        return {
            "_id": self._id,
            "game_id": self.game_id,
            "outside_hitter_1": self.outside_hitter_1,
            "position_2": self.position_2,
            "position_3": self.position_3,
            "years": self.years
        }

    def insert_to_teams(self):
        Database.insert_one(self.collection, self.json())



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
