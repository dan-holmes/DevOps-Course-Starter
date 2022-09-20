from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_items, add_item, resolve_item
from todo_app.flask_config import Config
from todo_app.data.ViewModel import ViewModel


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        item_view_model = ViewModel(get_items())
        return render_template('index.html', view_model=item_view_model)

    @app.route('/new', methods=['GET', 'POST'])
    def create():
        add_item(request.form.get('name'))
        return redirect('/')

    @app.route('/resolve/<id>')
    def resolve(id):
        resolve_item(id)
        return redirect('/')

    return app