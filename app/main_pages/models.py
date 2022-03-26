from app.extensions.database import db

class User(UserMixin, db.Model):
    id= db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index = True, unique = True)
    password = db.Column(db.String(100))

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    task = db.Column(db.String(200), index = True)


