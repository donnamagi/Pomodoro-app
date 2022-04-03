from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from app.classes import RegisterForm, LoginForm
from app.extensions.database import db


blueprint = Blueprint('main_pages', __name__)

##################

@blueprint.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', title = 'Pomodoro app')

@blueprint.route('/user', methods= ['GET', 'POST'])
def authentication():
    return render_template('authentication.html', title = 'Sign in')

@blueprint.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.password.data != form.password2.data:
        flash('Make sure you enter the same password')

    if form.validate_on_submit():
        print('form validated')
        user = User(username = form.username.data)
        print(user)
        print(user.username)
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()
            print('commit done')
            login_user(user)
            return redirect(url_for('main_pages.index'))
        except:
            flash('Error')
            db.session.rollback()
            
        # if not User.query.get(form.username.data):
        #     flash('This username is already taken.')

    return render_template('registration.html', form = form, title = 'Register')

@blueprint.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        next_url = form.next_url.data
        user = User.query.filter_by(username = form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(next_url) or url_for('main_pages.index')

        else:
            flash('Register first')

    return render_template('login_page.html', form = form, title = 'Login')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_pages.index'))
