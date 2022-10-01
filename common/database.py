import pymongo
import os
from dotenv import load_dotenv


class Database:
    load_dotenv()
    MONGO_URI = os.getenv("MONGO_URI")
    DATABASE = pymongo.MongoClient(MONGO_URI)["pickup-volleyball"]

    @staticmethod
    def insert_one(collection: str, data: dict):
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection: str, query: dict) -> pymongo.cursor:
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection: str, query: dict) -> dict:
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update(collection: str, query: dict, data: dict) -> None:
        Database.DATABASE[collection].update(query, data, upsert=True)  # update or insert

    @staticmethod
    def remove(collection: str, query: dict) -> dict:
        return Database.DATABASE[collection].remove(query)