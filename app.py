from flask import Flask, render_template, url_for

# from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin, current_user


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def index():

    return render_template('index.html', title = "Pomodoro app")

@app.route('/todolist')
def todolist():

    return render_template('todolist.html', title = "Pomodoro app")

@app.route('/login', methods= ['GET', 'POST'])
def login():
    return render_template('login.html', title = "Pomodoro app")



# For future reference

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))