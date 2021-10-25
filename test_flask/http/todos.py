import json
from dataclasses import dataclass

from flask import Response, jsonify, request
from flask.views import MethodView, View

from db import Database
from test_flask.utils import defaulthandler


class Todos():
    db = Database()

    def getTodos(self):
        return Response(json.dumps(self.db.fetchrows("""SELECT * from todos"""), default=defaulthandler), mimetype='application/json'), 200

    def getTodo(self, id):
        return Response(json.dumps(self.db.fetchrow("""SELECT * from todos WHERE id={0}""".format(id)), default=defaulthandler), mimetype='application/json'), 200

    def insertTodo(self):        
        title = request.get_json().get("title")
        self.db.insertrow("""INSERT INTO todos(title, completed) VALUES ('{0}', FALSE)""".format(title))        
        return self.getTodos()
