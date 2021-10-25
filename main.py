import os

from db import Database
from test_flask import app
from test_flask.http import Todos

database = Database()
database.connect()

todos = Todos()

app.add_url_rule('/todos', 'todos', todos.getTodos, methods=['GET'])
app.add_url_rule('/todos', 'inserttodo', todos.insertTodo, methods=['POST'])
app.add_url_rule('/todos/<int:id>', 'todo', todos.getTodo, methods=['GET'])

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=os.getenv('FLASK_RUN_PORT'))
