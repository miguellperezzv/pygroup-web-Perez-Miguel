from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField

class CreateGenreForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

class CreateProductForm(FlaskForm):
    nameProduct = StringField('Product name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])