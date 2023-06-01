import os
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app

import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client

collection = mongomock.MongoClient()[os.getenv('MONGO_DATABASE_NAME')][os.getenv('MONGO_COLLECTION_NAME')]

def test_index_page(monkeypatch, client):
    collection.insert_one({
        'name': 'Test card',
        'status_id': 1,
        'created_at': '2021-01-01T00:00:00.000Z'
    })

    print(os.getenv('MONGO_CONNECTION_STRING'))
    
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

