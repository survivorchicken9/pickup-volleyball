import uuid
from common.database import Database
from dataclasses import dataclass, field


@dataclass(eq=False)
class Player:
    collection: str = field(init=False, default="players")
    game_id: str
    position_1: str
    position_2: str
    position_3: str
    years: int
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> dict:
        return {
            "_id": self._id,
            "collection": self.collection,
            "game_id": self.game_id,
            "position_1": self.position_1,
            "position_2": self.position_2,
            "position_3": self.position_3,
            "years": self.years
        }

    def insert_to_players(self):
        Database.insert_one(self.collection, self.json())
