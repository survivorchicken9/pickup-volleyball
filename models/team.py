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
    opposite_hitter: str
    setter: str
    libero: str
    middle_blocker_2: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> dict:
        return {
            "_id": self._id,
            "game_id": self.game_id,
            "outside_hitter_1": self.outside_hitter_1,
            "outside_hitter_2": self.outside_hitter_2,
            "middle_blocker_1": self.middle_blocker_1,
            "middle_blocker_2": self.middle_blocker_2,
            "opposite_hitter": self.opposite_hitter,
            "setter": self.setter,
            "libero": self.libero,
        }

    def insert_to_teams(self):
        Database.insert_one(self.collection, self.json())
