import os
from todo_app.data.ItemStatus import ItemStatus

class Item:

    def __init__(self, id, name, status_id, created_at):
        self.id = str(id)
        self.name = name
        self.status = self._getItemStatus(status_id)
        self.created_at = created_at

    def resolved(self):
        return self.status == 'DONE'

    def _getItemStatus(_, status_id):
        if status_id == 1:
            return ItemStatus.TODO
        elif status_id == 3:
            return ItemStatus.DOING
        elif status_id == 2:
            return ItemStatus.DONE
        else:
            raise ValueError('Invalid status')