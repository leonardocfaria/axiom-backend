import pymongo
from notes_features.utils.config import config
from notes_features.constants.constants import (DATABASE_NAME)

class MongoDBHandler:
    def __init__(self):
        self.client = pymongo.MongoClient(config.credentials.mongodb_uri)
        self.db = self.client[DATABASE_NAME]

    def create(self, collection, data):
        return self.db[collection].insert_one(data).inserted_id
    
    def read_one(self, collection, query):
        return self.db[collection].find_one(query)
    
    def read_many(self, collection, query):
        cursor = self.db[collection].find(query)
        return list(cursor)
    
    def delete(self, collection, query):
        return self.db[collection].delete_many(query)
    
    def update(self, collection, query, field, data):
        return self.db[collection].update_one(query, {"$set": {field: data}})

