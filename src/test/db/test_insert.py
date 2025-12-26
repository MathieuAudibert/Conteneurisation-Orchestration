from cfg.db.classes.doctrine import Doctrine

d = Doctrine()
pgt = d.insert("cars", [{"brand": "peugeot"}])
print(f"[INFO]: inserted - {pgt}")