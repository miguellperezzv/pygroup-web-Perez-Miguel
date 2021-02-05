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
    #description = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())



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
    image = db.Column(db.String(500), default="https://discussions.apple.com/content/attachment/881765040")

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    release_id=db.Column(db.Integer, db.ForeignKey('release.id'))
    format_id=db.Column(db.Integer, db.ForeignKey('format.id'))
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        fields = ["id", "name"]

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Product
        fields = ["id", "release", "format", "artist", "price", "weight", "description", "image"] 


class ArtistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Artist
        fields = ["id", "name", "description"]

class ReleaseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Release
        fields = ["name", "artist_id", "genre_id", "imagen", "release_date"]


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

def get_all_artists():
    artists_qs = Artist.query.all()
    artist_schema = ArtistSchema()
    artists = [artist_schema.dump(artist) for artist in artists_qs]
    return artists

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

def get_artist_by_name(name):
    artist_qs = Artist.query.filter_by(name=name).first()
    artist_schema = ArtistSchema()
    a = artist_schema.dump(artist_qs)
    return a

#inviable
'''
def get_artists_by_genre(id):
    artist_qs = Artist.query.filter_by(genre_id=id)
    artist_schema = ArtistSchema()
    a = [artist_schema.dump(artist) for artist in artist_qs ]
    return a
'''

def get_releases_by_genre(id):
    releases_qs = Release.query.filter_by(genre_id=id)
    release_schema = ReleaseSchema()
    releases=[release_schema.dump(release) for release in releases_qs]
    return releases

def get_releases_by_artist(id):
    releases_qs = Release.query.filter_by(artist_id=id)
    release_schema = ReleaseSchema()
    releases=[release_schema.dump(release) for release in releases_qs]
    return releases

def get_single_release_by_artist(id,name):
    release_qs = Release.query.filter_by(artist_id=id, name=name).first()
    release_schema = ReleaseSchema()
    r = release_schema.dump(release_qs)
    return r

def get_genre_by_name(name):
    genre_qs = Genre.query.filter_by(name=name).first()
    genre_schema = GenreSchema()
    g = genre_schema.dump(genre_qs)
    return g

def get_genre_by_id(id):
    genre_qs = Genre.query.filter_by(id=id).first()
    genre_schema = GenreSchema()
    g = genre_schema.dump(genre_qs)
    return g

def create_new_artist(name, description):
    artist = Artist(name=name, description=description)
    db.session.add(artist)

    if db.session.commit():
        return artist
    return None 

def create_new_release(artist_id, name, genre_id, release_date, image):
    release = Release(artist_id=artist_id, name=name, genre_id=genre_id, release_date=release_date, imagen=image)
    db.session.add(release)

    if db.session.commit():
        return release
        print("release añadido exitosamente!!!")
    return None 