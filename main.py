from flask import Flask, jsonify
from flask import Flask, jsonify
from flask.views import MethodView


app = Flask(__name__)

class TodoAPI:
    def __init__(self):
        self.todos = []

    def get_todos(self):
        return jsonify(self.todos)

    def create_todo(self, data):
        self.todos.append(data)
        return jsonify({'message': 'Todo created'})

todo_view = TodoAPI.as_view('todo_api')
app.add_url_rule('/todos', view_func=todo_view, methods=['GET', 'POST'])