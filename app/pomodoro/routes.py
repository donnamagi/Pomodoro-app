from flask import Blueprint, Flask, render_template, url_for, flash, redirect
from app import classes
from app.extensions.database import db
from flask_login import current_user
from app.main_pages.models import Todos

blueprint = Blueprint('pomodoro', __name__)


todos = []

@blueprint.route('/todolist', methods = ['GET', 'POST'])
def todolist():
    global todos
    form = classes.SubmitForm()

    if form.validate_on_submit():

        if current_user.is_authenticated:
            id = current_user.id
            tasks = Todos.query.filter_by(user_id = id).all()     
            task = Todos(task = form.todo.data, user_id = id)
            try:
                db.session.add(task)
                db.session.commit()  
                flash('Task added!')
            except:
                db.session.rollback()
                flash('Error')
        else:
            todos.append(form.todo.data)
            flash('Task added!')

    return render_template('todolist.html', title = 'Todo list', form = form, todos = todos)


@blueprint.route('/delete/<task>')
def delete(task):

    todos.remove(task)
    
    return redirect(url_for('pomodoro.todolist')), flash("Entry deleted")

