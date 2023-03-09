import os
import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    if (os.getenv('ENVIRONMENT') != 'docker'):
        file_path = find_dotenv('.env.test')
        load_dotenv(file_path, override=True)

    # Create the new app.
    test_app = app.create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data

def get_lists_stub(method, url, headers={}, params={}):
    test_board_id = os.environ.get('TRELLO_BOARD_ID')
    fake_response_data = None
    if url == f'https://api.trello.com/1/boards/{test_board_id}/cards':
        fake_response_data = [
                {
                    'id': '456',
                    'name': 'Test card',
                    'start': '2022-01-01',
                    'idList': os.getenv('TRELLO_TODO_LIST_ID')
                }
            ]
        return StubResponse(fake_response_data)

    raise Exception(f'Integration test did not expect URL "{url}"')

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'request', get_lists_stub)
    response = client.get('/')

    assert response.status_code == 200
    assert 'Test card' in response.data.decode()

