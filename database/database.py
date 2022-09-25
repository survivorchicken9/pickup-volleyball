import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("PYMONGO_USER")
PASSWORD = os.getenv("PYMONGO_PASSWORD")


def get_client():
    client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@pickup-volleyball.pbcjy4r.mongodb.net/?retryWrites"
                                 f"=true&w=majority")
    return client

def test_client():
    client = get_client()
    print(client.test)
    client.close()

def insert_to_players():
    client = get_client()
    db = client["pickup-volleyball"]
    players_collection = db["players"]
    test = {
        "id": 344141,
        "game_id": 1,
        "name": "Chris",
        "pos1": "Outside Hitter",
        "pos2": "Middle Blocker",
        "pos3": "Setter"
    }
    players_collection.insert_one(test)
    client.close()


insert_to_players()

# collections = ["games", "players", "teams", "admin"]
