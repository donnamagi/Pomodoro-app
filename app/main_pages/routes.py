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

@blueprint.route('/register', methods= ['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.password.data != form.password2.data:
        flash('Make sure you enter the same password')

    if form.validate_on_submit():
        
        user = User(username = form.username.data)
        user.set_password(form.password.data)

        try:
            db.session.add(user)
            db.session.commit()
            # login_user(user)
            return redirect(url_for('main_pages.index'))
        except:
            db.session.rollback()
            
        if not User.query.get(form.email.data):
            flash('This email is already in use.')

        
    return render_template('registration.html', form = form, title = 'Register')

# For future reference

# @blueprint.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('main_pages.login'))
