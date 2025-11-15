import os
from pymongo import MongoClient
from dotenv import load_dotenv

class ConnectDb:
    def __init__(self, uri: str, db_name: str):
        self.uri = uri
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.uri)
            self.db = self.client[self.db_name]
            print("[INFO]: succesfully connected to db")
        except Exception as e:
            print(f"[ERROR]: error while connecting to db - {e}")

load_dotenv()
con = ConnectDb(uri=os.getenv("MONGO_URI"), db_name="Cars")
# con.connect() test