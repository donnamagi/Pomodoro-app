from flask import Blueprint, render_template, url_for, redirect
from .models import User

blueprint = Blueprint('main_pages', __name__)

##################

@blueprint.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', title = 'Pomodoro app')

@blueprint.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html', title = 'Login')

# For future reference

# @blueprint.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('main_pages.login'))
