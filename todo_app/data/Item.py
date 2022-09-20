import os
from todo_app.data.ItemStatus import ItemStatus

class Item:

    def __init__(self, id, name, status, created_at):
        self.id = id
        self.name = name
        self.status = status
        self.created_at = created_at

    def resolved(self):
        return self.status == ItemStatus.DONE

    @classmethod
    def from_json_object(cls, json_object):
        return Item(
            json_object['id'],
            json_object['name'],
            cls._getStatusFromListId(json_object['idList']),
            json_object['start']
        )
    
    @classmethod
    def _getStatusFromListId(_, list_id):
        if list_id == os.getenv('TRELLO_TODO_LIST_ID'):
            return ItemStatus.TODO
        elif list_id == os.getenv('TRELLO_DONE_LIST_ID'):
            return ItemStatus.DONE
        else:
            raise Exception('Invalid list id')