from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

documents = db.all()
print(db.contains(doc_id=199))