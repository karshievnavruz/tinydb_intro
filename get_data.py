from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

doc = db.get(doc_id=4)
print(doc)