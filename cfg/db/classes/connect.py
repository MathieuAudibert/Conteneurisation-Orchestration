import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

class ConnectDB:
    def __init__(self, adm: bool):
        self.uri = os.getenv("ADM_MONGO_URI") if adm else os.getenv("MONGO_URI", "")
        self.db_name = "Cars" 
        self.client = None
        self.db = None
        self.adm = adm

    def connect(self):
        try:
            if self.adm == True:
                self.client = MongoClient(self.uri)
                self.db = self.client[self.db_name]
                print("[INFO]: succesfully connected to db as **ADMIN**")
            else: 
                self.client = MongoClient(self.uri)
                self.db = self.client[self.db_name]
                print("[INFO]: succesfully connected to db as **READ ONLY**")
        except Exception as e:
            print(f"[ERROR]: error while connecting to db - {e}")
    
    def disconnect(self):
        try:
            self.client.close()
            print("[INFO]: disconnected successfully")
        except Exception as e:
            print(f"[ERROR]: error while disconnecting to db - {e}")

"""
con_adm = ConnectDB(adm=True)
con_adm.connect()
con_adm.disconnect()

con_ro = ConnectDB(adm=False)
con_ro.connect()
con_ro.disconnect()
"""