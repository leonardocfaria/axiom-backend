import pymongo
from dotenv import load_dotenv
from notes_features.utils.config import config
from notes_features.constants.constants import (DATABASE_NAME)

class MongoDBHandler:
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb+srv://lcfaria:200805Lf.@cluster0.5imi7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        self.db = self.client[DATABASE_NAME]

    def create(self, collection, data):
        return self.db[collection].insert_one(data).inserted_id
    
    def read_one(self, collection, query):
        return self.db[collection].find_one(query)