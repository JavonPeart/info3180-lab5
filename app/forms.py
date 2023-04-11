# Add any form classes for Flask-WTF here

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed, DataRequired


class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    poster = FileField('File', validators=[FileAllowed(['jpg','png'], 'Images only!')])
