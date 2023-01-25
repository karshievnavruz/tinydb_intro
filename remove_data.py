from tinydb import TinyDB
db = TinyDB('db.json',indent=4)

db.truncate()