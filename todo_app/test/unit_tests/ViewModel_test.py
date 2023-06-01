import datetime
from todo_app.data.ViewModel import ViewModel
from todo_app.data.Item import Item
from todo_app.data.ItemStatus import ItemStatus

doing_item = Item(1, 'Doing Item', ItemStatus.DOING.value, datetime.datetime.now())
doing_item_2 = Item(1, 'Doing Item 2', ItemStatus.DOING.value, datetime.datetime.now())
todo_item = Item(1, 'ToDo Item', ItemStatus.TODO.value, datetime.datetime.now())
done_item = Item(1, 'Done Item', ItemStatus.DONE.value, datetime.datetime.now())

items = [doing_item, doing_item_2, todo_item, done_item]

def test_doing_items():
    item_view_model = ViewModel(items)

    assert len(item_view_model.doing_items) == 2
    assert doing_item in item_view_model.doing_items
    assert doing_item_2 in item_view_model.doing_items

def test_todo_items():
    item_view_model = ViewModel(items)

    assert len(item_view_model.todo_items) == 1
    assert todo_item in item_view_model.todo_items

def test_done_items():
    item_view_model = ViewModel(items)

    assert len(item_view_model.done_items) == 1
    assert done_item in item_view_model.done_items
