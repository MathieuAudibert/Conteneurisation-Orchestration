from cfg.db.classes.doctrine import Doctrine

d = Doctrine()
ctr = d.update('cars', filter={'brand': 'peugeot'}, update=[{'brand': 'citroen'}])
print(f"[INFO]: created - {ctr}")