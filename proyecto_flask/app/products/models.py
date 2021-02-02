from app.db import db, ma
from datetime import datetime



class Artist(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())

class Release(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    name  = db.Column(db.String(200), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    release_date = db.Column(db.DateTime, default= datetime.now())
    imagen = db.Column(db.String(500), default="https://discussions.apple.com/content/attachment/881765040")
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())

class Format(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())


'''
class Product(db.Model):
    """
    Documentación 
    """

    id = db.Column(db.Integer, primary_key= True)
    release_id = db.Column(db.Integer, db.ForeignKey("release.id") )
    format_id = db.Column(db.Integer, db.ForeignKey("format.id"))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    price =  db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, default = 1)
    description = db.Column(db.String(500),nullable=True )
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())
    #imagen = db.Column(db.String(500), default="https://discussions.apple.com/content/attachment/881765040")
'''
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    release_id=db.Column(db.Integer, db.ForeignKey('release.id'))
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
'''
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Product
        fields = ["id", "release", "format", "artist", "price"] 
'''

class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artist
        fields = ["id", "nameArtist", "description"]

class ReleaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Release
        fields = ["name", "artist", "genre", "image"]


def get_all_genres():
    genres_qs  = Genre.query.all()
    genre_schema = GenreSchema()
    genres =[genre_schema.dump(genre) for genre in genres_qs]
    return genres

def create_new_genre(name):
    genre = Genre(name=name)
    db.session.add(genre)

    if db.session.commit():
        return genre
    return None 

def get_all_products():
    products_qs = Product.query.all()
    product_schema = ProductSchema()
    products=[product_schema.dump(product) for product in products_qs]
    return products

def get_all_releases():
    releases_qs = Release.query.all()
    release_schema = ReleaseSchema()
    releases=[release_schema.dump(release) for release in releases_qs]
    return releases


def  create_new_product(name,price, weight, genre_id, image):
    
    #genre = db.session.query.filter(id==genre_id)

    #if genre != []:
    #    return {"info ":ok}
    #return {"No hay info ":Bad}

    product = Product(name=name, price=price,genre_id=genre_id, image=image)
    db.session.add(product)

    if db.session.commit():
        return genre
    return None 


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id==id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    return p

def create_new_artist(name, description):
    artist = Artist(name=name, description=description)
    db.session.add(artist)

    if db.session.commit():
        return artist
    return None 

def create_new_release(artist_id, name, genre_id, release_date, image):
    artist = Artist(artist_id=artist_id, name=name, genre_id=genre_id, release_date=release_date, image=image)
    db.session.add(artist)

    if db.session.commit():
        return artist
    return None 