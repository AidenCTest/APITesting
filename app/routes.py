from flask import Blueprint, request, jsonify
from . import db
from .models import User, Project, Task
from .schemas import UserSchema, ProjectSchema, TaskSchema

main = Blueprint('main', __name__)

user_schema = UserSchema()
project_schema = ProjectSchema()
task_schema = TaskSchema()

def commit_and_respond(instance, schema):
    db.session.add(instance)
    db.session.commit()
    return jsonify(schema.dump(instance)), 201

# User registration
@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    return commit_and_respond(user, user_schema)

# Project CRUD
@main.route('/projects', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Project(name=data['name'], description=data.get('description'))
    return commit_and_respond(project, project_schema)

@main.route('/projects', methods=['GET'])
def list_projects():
    projects = Project.query.all()
    return jsonify(project_schema.dump(projects, many=True))

@main.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify(project_schema.dump(project))

@main.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.get_json()
    project.name = data.get('name', project.name)
    project.description = data.get('description', project.description)
    db.session.commit()
    return jsonify(project_schema.dump(project))

@main.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    return '', 204

# Task CRUD
@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task = Task(title=data['title'], description=data.get('description'), status=data.get('status', 'pending'), user_id=data.get('user_id'), project_id=data.get('project_id'))
    return commit_and_respond(task, task_schema)

@main.route('/tasks', methods=['GET'])
def list_tasks():
    # TODO: Add filtering by status, project, user
    tasks = Task.query.all()
    return jsonify(task_schema.dump(tasks, many=True))

@main.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get_or_404(task_id)
    return jsonify(task_schema.dump(task))

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)  # Bug: does not check if user is assigned
    task.user_id = data.get('user_id', task.user_id)
    task.project_id = data.get('project_id', task.project_id)
    db.session.commit()
    return jsonify(task_schema.dump(task))

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return '', 204 