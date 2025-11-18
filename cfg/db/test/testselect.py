from cfg.db.classes.doctrine.select import DoctrineSelect

d = DoctrineSelect(False)
all_docs = d.select_all('cars')
print('[INFO]:', len(all_docs), 'documents found')
for doc in all_docs[:3]:
    print(doc)

toyotas = d.select_list('cars', filter={'brand': 'toyota'})
print('[INFO]:', toyotas)