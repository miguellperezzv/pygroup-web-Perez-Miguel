from app.db import db, ma
from datetime import datetime





class Product(db.Model):
    """
    Documentación 
    """

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable=False)
    price =  db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, default = 1)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())
    imagen = db.Column(db.String(500), default="https://discussions.apple.com/content/attachment/881765040")


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Product
        fields = ["id", "name", "price", "imagen"] 

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datetime.now())
    updated_at = db.Column(db.DateTime, default= datetime.now())


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


def  create_new_product(name,price, weight, genre_id, image):
    genre = db.session.query.filter(id==genre_id)

    if genre != []:
        return {"info ":ok}
    return {"No hay info ":Bad}


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id==id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    return p