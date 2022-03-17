from flask import Flask, render_template, url_for, flash, redirect
from . import pomodoro

# from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'


app.register_blueprint(pomodoro.routes.blueprint)

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