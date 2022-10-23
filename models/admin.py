import uuid
from common.database import Database
from dataclasses import dataclass, field


@dataclass(eq=False)
class Admin:
    collection: str = field(init=False, default="admin")
    username: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymouse(self):
        return False

    def get_id(self) -> str:
        return str(Database.find_one(self.collection, {"username": self.username})["_id"])

    @classmethod
    def get_all_admins(cls):
        return [cls(**elem).json() for elem in Database.find(cls.collection, {})]

    @classmethod
    def find_admin(cls, username: str):
        return Database.find_one(cls.collection, {"username": username})

    def json(self) -> dict:
        return {
            "_id": self._id,
            "name": self.username,
            "password": self.password
        }

    def insert_to_admins(self):
        Database.insert_one(self.collection, self.json())
        print("inserted")
