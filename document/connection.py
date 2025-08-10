from pymongo.mongo_client import MongoClient

def get_mongo_client():
    client = MongoClient("mongodb://root:example@localhost:27017/?authSource=admin")
    return client