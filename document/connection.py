from pymongo.mongo_client import MongoClient

client = MongoClient('localhost', 27017)

try:
    client.admin.command('ping')
    
    print("pong")
except Exception as e:
    print(e)