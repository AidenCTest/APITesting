from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    tasks = db.relationship('Task', backref='assignee', lazy=True)

    def __init__(self, username, email, password_hash=None):
        self.username = username
        self.email = email
        if password_hash:
            self.password_hash = password_hash

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    tasks = db.relationship('Task', backref='project', lazy=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def __init__(self, title, description=None, status='pending', user_id=None, project_id=None):
        self.title = title
        self.description = description
        self.status = status
        self.user_id = user_id
        self.project_id = project_id 