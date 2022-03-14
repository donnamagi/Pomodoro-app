from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class SubmitForm(FlaskForm):
    todo = StringField('Todo:', validators= [DataRequired()])
    submit = SubmitField('Add task')

class RegisterForm(FlaskForm):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    password2 = PasswordField('repeat password', validators = [DataRequired(), EqualTo('password', message= 'Passwords must match.')])
    submit = SubmitField ('Register')