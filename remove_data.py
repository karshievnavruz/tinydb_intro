from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

print(db.remove(doc_ids=[5,6]))