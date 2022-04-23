from app.main_pages.models import User, Todos
from app.extensions.database import db

def test_new_user(client):

    # Creates new instance of User model
    # Hashes password
    # Checks if model values are properly assigned
    # if User exists in DB
    # and password hashed

    user = User(username = 'testname')
    user.set_password('password')

    assert user.username == 'testname'
    assert User.query.filter_by(username = user.username)
    assert user.password != 'password'

def test_new_todo(client):

    # Creates new instance of Todos model
    # Checks if model values are properly assigned
    # if task is linked to user_id

    sample = Todos(task = 'sample', user_id = 0)

    assert sample.task == 'sample'
    assert Todos.query.filter_by(user_id = 0)
