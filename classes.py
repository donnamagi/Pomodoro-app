from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo

class SubmitForm(FlaskForm):
    todo = StringField('Todo:', validators= [DataRequired()])
    submit = SubmitField('Add task')