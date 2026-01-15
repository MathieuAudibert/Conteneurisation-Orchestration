from src.core.db.doctrine import Doctrine

d = Doctrine()
pgt = d.insert("cars", [{"brand": "peugeot"}])
print(f"[INFO]: inserted - {pgt}")