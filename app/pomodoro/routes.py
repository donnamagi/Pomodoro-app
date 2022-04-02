from flask import Blueprint, Flask, render_template, url_for, flash, redirect
from app import classes
from app.extensions.database import db
from flask_login import current_user, login_required
from app.main_pages.models import Todos

blueprint = Blueprint('pomodoro', __name__)



@blueprint.route('/todolist', methods = ['GET', 'POST'])
@login_required
def todolist():

    id = current_user.id
    todos = current_user.todos.all()
    form = classes.SubmitForm()
    
    if form.validate_on_submit():

        task = Todos(task = form.todo.data, user_id = id)

        try:
            db.session.add(task)
            db.session.commit()  
            flash('Task added!')
            return redirect(url_for('pomodoro.todolist'))
        except:
            db.session.rollback()
            flash('Error')

    return render_template('todolist.html', title = 'Todo list', form = form, todos = todos)


@blueprint.route('/delete/<task>')
def delete(task):

    todos.remove(task)
    
    return redirect(url_for('pomodoro.todolist')), flash("Entry deleted")

