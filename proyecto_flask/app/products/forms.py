from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import DateField, SelectField
from datetime import date, datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.products.models import Artist, Genre
from app.products import models

class CreateGenreForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])


class CreateProductForm(FlaskForm):
    nameProduct = StringField('Product name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])

class CreateArtistForm(FlaskForm):
    name = StringField('Artist name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])

class CreateReleaseForm(FlaskForm):
    artist_id=QuerySelectField(query_factory=lambda: Artist.query.all(),get_label="name")
    name = StringField('Release Name', validators=[DataRequired()])
    genre_id=QuerySelectField(query_factory=lambda: Genre.query.all(),get_label="name")
    release_date = DateField('Release Date', format='%Y%m/%d')
    #release_date = DateTimeField('Release Date', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
