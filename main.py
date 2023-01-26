from tinydb import TinyDB
from tinydb.table import Document
import requests
TOKEN = '5503823244:AAFNZ-echSZpypl7dIKeeMLroXN7OBraNHo'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

db = TinyDB('db.json',indent=4)
print(db.default_table_name)


response = requests.get(url=BASE_URL)
updates=response.json()['result']
 
for update in updates:
    msg = update['message']
    message_id=msg['message_id']
    id=(msg['from']['id'])
    first_name=(msg['from']['first_name'])
    
id1= message_id
a=((db.contains(doc_id=id1)))
print(a)

if a==False:
       user = Document({
          'firstname':first_name,
          'id':id
       },doc_id=id1)
       db.insert(user)
else:
   i=0
   while i<id1:
    id1=id1+1
    b=((db.contains(doc_id=id1)))

    if b==False:
        user=Document({
          'firstname':first_name,
          'id':id
       },doc_id=id1)
        db.insert(user)
        break
    i=i+1