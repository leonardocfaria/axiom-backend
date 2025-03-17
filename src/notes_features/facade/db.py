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