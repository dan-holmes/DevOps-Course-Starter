import requests
import os
from todo_app.data.Item import Item

base_url = "https://api.trello.com/1"

headers = {
   "Accept": "application/json"
}

query = {
   'key': os.getenv('TRELLO_API_KEY'),
   'token': os.getenv('TRELLO_API_TOKEN'),
}

def get_items():
    board_id = os.getenv('TRELLO_BOARD_ID')
    response = requests.request(
        "GET",
        base_url + f'/boards/{board_id}/cards',
        headers=headers,
        params = {
            **query,
        }
    )
    return list(map(Item.from_json_object, response.json()))

def add_item(name):
    requests.request(
        "POST",
        base_url + '/cards',
        headers = headers,
        params = {
            **query,
            'idList': os.getenv('TRELLO_TODO_LIST_ID'),
            'name': name
        }
    )

def resolve_item(id):
    response = requests.request(
        "PUT",
        base_url + f'/cards/{id}',
        headers = headers,
        params = {
            **query,
            'idList': os.getenv('TRELLO_DONE_LIST_ID')
        }
    )
    print(response.text)
