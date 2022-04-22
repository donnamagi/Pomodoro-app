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

@blueprint.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.password.data != form.password2.data:
        flash('Make sure you enter the same password')

    if form.validate_on_submit():

        #Error message for the user
        if User.query.filter_by(username = form.username.data).first():
            flash('This username is already taken.')
            return redirect(url_for('main_pages.register'))

        #Creating database entry
        user = User(username = form.username.data)
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('main_pages.index'))
        except Exception as error_message:
            print(error_message)
            flash('Error')
            db.session.rollback()

    return render_template('registration.html', form = form, title = 'Register')

@blueprint.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        #Checking if user exists
        user = User.query.filter_by(username = form.username.data).first()
        if not user:
            flash('Register first')
            return redirect(url_for('main_pages.login'))

        if user and user.check_password(form.password.data):
            login_user(user)

            #If applicable, next_url will enable user to continue where they were before they got rerouted to login
            next_url = form.next_url.data
            if next_url != '':
                return redirect(next_url)

            return redirect(url_for('pomodoro.todolist'))

        else:
            flash('Are you sure you entered the right password?')

    return render_template('login_page.html', form = form, title = 'Login')


@blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main_pages.index'))
