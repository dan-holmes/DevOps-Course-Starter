from todo_app.data.ItemStatus import ItemStatus

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def doing_items(self):
        return list(filter(lambda item: item.status == ItemStatus.DOING, self._items))

    @property
    def todo_items(self):
        return list(filter(lambda item: item.status == ItemStatus.TODO, self._items))

    @property
    def done_items(self):
        return list(filter(lambda item: item.status == ItemStatus.DONE, self._items))