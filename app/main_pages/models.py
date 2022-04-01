from app.extensions.database import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique = True)
    password = db.Column(db.String(100))
    todos = db.relationship('Todos', backref = 'todos', lazy = True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task = db.Column(db.String(200), index = True)


