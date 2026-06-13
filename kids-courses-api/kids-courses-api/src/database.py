from pymongo import MongoClient

class Database:
    def __init__(self, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client['kids_courses_db']

    def connect(self):
        return self.db

    def disconnect(self):
        self.client.close()