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
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> dict:
        return {
            "_id": self._id,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "location": self.location,
            "notes": self.notes
        }

    def insert_to_games(self):
        Database.insert_one(self.collection, self.json())

    @classmethod
    def get_all_games(cls):
        print([cls(**elem).json() for elem in Database.find(cls.collection, {})])
