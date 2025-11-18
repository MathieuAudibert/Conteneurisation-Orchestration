from typing import Any, Dict, Optional
from cfg.db.classes.connect import ConnectDB
import pymongo

def _serialize(doc: Dict[str, Any]):
	# a implementer si j'ai pas la flm
	return doc

class DoctrineSelect:
	# CHANGEME: pour moi la db doit etre lisible que en readonly 
	def __init__(self, adm: bool=False):
		self.conn = ConnectDB(adm=adm)
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
			print(f"[ERROR] Doctrine.select_all: {e}")
			return []

	def select_list(self, collection_name: str, filter: Optional[Dict[str, Any]] = None, projection: Optional[Dict[str, Any]] = None):
		# projection = champs a select
		try:
			coll = self._get_collection(collection_name)
			cursor = coll.find(filter or {}, projection)
			data = list(cursor)
			return [_serialize(d) for d in data]
		except Exception as e:
			print(f"[ERROR] Doctrine.select_list: {e}")
			return []
