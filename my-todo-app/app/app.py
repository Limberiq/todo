from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db/todo'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(80), nullable=False)

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()  # Используем метод all() на объекте запроса
    return jsonify([{"id": todo.id, "task": todo.task} for todo in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.json['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({"id": new_todo.id, "task": new_todo.task})

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')