from flask import Blueprint, Flask, render_template, url_for, flash, redirect
from app import classes

blueprint = Blueprint('pomodoro', __name__)


todos = []

@blueprint.route('/todolist', methods = ['GET', 'POST'])
def todolist():

    form = classes.SubmitForm()
    
    if form.validate_on_submit():
        todos.append(form.todo.data)
        flash('Task added!')


    return render_template('todolist.html', title = 'Todo list', form = form, todos = todos)


@blueprint.route('/delete/<task>')
def delete(task):

    todos.remove(task)
    
    return redirect(url_for('todolist')), flash("Entry deleted")

