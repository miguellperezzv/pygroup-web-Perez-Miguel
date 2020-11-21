from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField

class CreateGenreForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
