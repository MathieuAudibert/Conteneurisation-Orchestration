from typing import Any, Dict, Optional
from cfg.db.classes.connect import ConnectDB
import pymongo

def _serialize(doc: Dict[str, Any]):
    # a implementer si j'ai pas la flm
    return doc

class Doctrine:
    def __init__(self):
        self.conn = ConnectDB(False)
        self.conn.connect()

    def _get_collection(self, collection_name: str):
        if getattr(self.conn, "db", None) is None:
            raise RuntimeError("[ERROR]: not connected to db")
        return self.conn.db[collection_name]

    def select_all(self, collection_name: str):
        try:
            collection = self._get_collection(collection_name)
            data = list(collection.find({}))
            return [_serialize(d) for d in data]
        except Exception as e:
            print(f"[ERROR] Doctrine.select_all - {e}")
            return []

    def select_list(self, collection_name: str, filter: Optional[Dict[str, Any]] = None, projection: Optional[Dict[str, Any]] = None):
        # projection = champs a select
        try:
            coll = self._get_collection(collection_name)
            cursor = coll.find(filter or {}, projection)
            data = list(cursor)
            return [_serialize(d) for d in data]
        except Exception as e:
            print(f"[ERROR] Doctrine.select_list - {e}")
            return []

    def insert(self, collection_name: str, args: Dict[str, Any]=None):
        self.conn.set_adm(True)
        try:
            if args is None:
                print("[ERROR] Doctrine.insert: no data provided")
                return None
            coll = self._get_collection(collection_name)

            if isinstance(args, list):
                res = coll.insert_many(args)
                return res.inserted_ids
            else:
                res = coll.insert_one(args)
                return res.inserted_id

        except Exception as e:
            print(f"[ERROR] Doctrine.insert - {e}")
            return None

        finally:
            try:
                self.conn.set_adm(False)
            except Exception as e2:
                print(f"[ERROR]: cant disable adm mode - {e2}")

    def update(self, collection_name: str, filter: Optional[Dict[str, Any]], update: Optional[Dict[str, Any]], many: bool=False):
        try:
            self.conn.set_adm(True)
            if update is None:
                print("[ERROR] Doctrine.update - no update gioven")
                return 0
            coll = self._get_collection(collection_name)

            if many:
                res = coll.update_many(filter or {}, {"$set": update})
                return res.modified_count
            else:
                res = coll.update_one(filter or {}, {"$set": update})
                return res.modified_count

        except Exception as e:
            print(f"[ERROR] Doctrine.update - {e}")
            return 0

        finally:
            try:
                self.conn.set_adm(False)
            except Exception as e2:
                print(f"[ERROR]: error while unseting adm - {e2}")

    def delete(self, collection_name: str, filter: Optional[Dict[str, Any]], many: bool=False):
        try:
            self.conn.set_adm(True)
            coll = self._get_collection(collection_name)

            if many:
                res = coll.delete_many(filter or {})
                return res.deleted_count

            else:
                res = coll.delete_one(filter or {})
                return res.deleted_count

        except Exception as e:
            print(f"[ERROR] Doctrine.delete - {e}")
            return 0

        finally:
            try:
                self.conn.set_adm(False)
            except Exception as e2:
                print(f"[ERROR]: unsetting adm - {e2}")