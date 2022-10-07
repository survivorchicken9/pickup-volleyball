import uuid
from common.database import Database
from dataclasses import dataclass, field


@dataclass(eq=False)
class Game:
    collection: str = field(init=False, default="games")
    date: str
    start_time: str
    end_time: str
    location: str
    notes: str
    number_of_teams: int = field(default=2)
    number_of_players: int = field(default=24)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def get_all_games(cls):
        return [cls(**elem).json() for elem in Database.find(cls.collection, {})]

    @classmethod
    def find_game(cls, game_id):
        return Database.find_one(cls.collection, {"_id": game_id})

    def json(self) -> dict:
        return {
            "_id": self._id,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location,
            "notes": self.notes,
            "number_of_teams": self.number_of_teams,
            "number_of_players": self.number_of_players
        }

    def insert_to_games(self):
        Database.insert_one(self.collection, self.json())
