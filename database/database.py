import pymongo
import os

# Get environment variables
USER = os.getenv("PYMONGO_USER")
PASSWORD = os.getenv("PYMONGO_PASSWORD")

client = pymongo.MongoClient(f"mongodb+srv://{USER}:{PASSWORD}@pickup-volleyball.pbcjy4r.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
