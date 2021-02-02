from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField
from wtforms import DateTimeField
from datetime import date, datetime


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
    artist_id = StringField('Artist ID', validators=[DataRequired()])
    name = StringField('Release Name', validators=[DataRequired()])
    genre_id = StringField('Genre ID', validators=[DataRequired()])
    
    '''
    release_date = DateTimeField('Release Date', validators=[DataRequired(),DateRange(
            min=datetime(1950, 1, 1),
            max=date.today())]  )
    '''
    release_date = DateTimeField('Release Date', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
