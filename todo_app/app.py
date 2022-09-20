from flask import Flask, render_template, redirect, request
from todo_app.data.trello_items import get_items, add_item, resolve_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    return render_template('index.html', items = get_items())

@app.route('/new', methods=['GET', 'POST'])
def create():
    add_item(request.form.get('name'))
    return redirect('/')

@app.route('/resolve/<id>')
def resolve(id):
    resolve_item(id)
    return redirect('/')