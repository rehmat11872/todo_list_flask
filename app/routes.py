from flask import Blueprint, request, jsonify
from . import db
from .models import User, Task

bp = Blueprint('main', __name__)

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "username": user.username}), 201

@bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data['title']
    description = data.get('description')
    user_id = data['user_id']
    task = Task(title=title, description=description, user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return jsonify({"id": task.id, "title": task.title, "description": task.description}), 201

@bp.route('/tasks/<int:user_id>', methods=['GET'])
def get_user_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([{"id": task.id, "title": task.title, "description": task.description, "completed": task.completed} for task in tasks])
