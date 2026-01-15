from src.core.db.doctrine import Doctrine

d = Doctrine()
spr = d.delete('cars', {'brand': 'peugeot'})
print(f"[INFO]: deleted - {spr}")