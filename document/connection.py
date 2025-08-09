from pymongo.mongo_client import MongoClient

def get_mongo_client():
    client = MongoClient('localhost', 27017)
    return client