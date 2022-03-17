from flask import Flask, render_template, url_for, flash, redirect
from . import pomodoro

# from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

def create_app():
  app = Flask(__name__)
  app.config.from_object('app.config')

  register_blueprints(app)

  return app

# Blueprint
def register_blueprints(app: Flask):
    app.register_blueprint(pomodoro.routes.blueprint)

# Main Routes
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', title = 'Pomodoro app')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html', title = 'Login')


# For future reference

# @blueprint.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))