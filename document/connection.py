from pymongo.mongo_client import MongoClient
from config import MONGO_URI

def get_mongo_client():
    client = MongoClient(MONGO_URI)
    return client