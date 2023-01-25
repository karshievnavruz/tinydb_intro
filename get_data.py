from tinydb import TinyDB
db = TinyDB('db.json',indent=4)
data = db.all()
print(type(data))