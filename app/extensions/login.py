from flask_login import LoginManager
from app.main_pages.models import User

login_manager = LoginManager()
login_manager.login_view = "main_pages.login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Implement anonymous users
# @login_manager.unauthorized_handler
# def unauthorized():
#     create a temporary user 
#     return redirect, user