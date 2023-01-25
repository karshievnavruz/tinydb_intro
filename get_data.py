from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

documents = db.all()
for doc in documents:
    print(doc)