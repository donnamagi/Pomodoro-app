from flask import Flask, render_template, url_for, flash
from classes import SubmitForm

# from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'

todos = []

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html', title = 'Pomodoro app')

@app.route('/todolist', methods = ['GET', 'POST'])
def todolist():

    form = SubmitForm()
    
    if form.validate_on_submit():
        todos.append(form.todo.data)
        flash('Task added!')


    return render_template('todolist.html', title = 'Todo list', form = form, todos = todos)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html', title = 'Login')



# For future reference

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))