import os
import pymongo
import certifi
import datetime
from todo_app.data.Item import Item
from todo_app.data.ItemStatus import ItemStatus

connection_string = os.getenv('MONGO_CONNECTION_STRING')
database_name = os.getenv('MONGO_DATABASE_NAME')
collection_name = os.getenv('MONGO_COLLECTION_NAME')

db = pymongo.MongoClient(os.getenv('MONGO_CONNECTION_STRING'), tlsCAFile=certifi.where())
database = db[os.getenv('MONGO_DATABASE_NAME')]
collection = database[os.getenv('MONGO_COLLECTION_NAME')]

def get_items():
    db_items = collection.find()
    items = []
    for item in db_items:
        items.append(Item(
            id=item['_id'],
            name=item['name'],
            status_id=item['status_id'],
            created_at=item['created_at']
        ))
    return items
    
def add_item(name):
    collection.insert_one({
        'name': name,
        'status_id': ItemStatus.TODO.value,
        'created_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    })

def resolve_item(id):
    collection.update_one(
        {'_id': id},
        {'$set': {'status_id': ItemStatus.DONE.value}}
    )
