from app.db import db, ma






class Product(db.Model):
    """
    Documentación 
    """

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(50), nullable=False)
    price =  db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, default = 1)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    created_at = db.Column(db.DataTime, default= datatime.now())
    updated_at = db.Column(db.DataTime, default= datatime.now())


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datatime.now())
    updated_at = db.Column(db.DateTime, default= datatime.now())


class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model= Product

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer, db.ForeignKey('product.id'))
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default= datatime.now())
    updated_at = db.Column(db.DateTime, default= datatime.now())


def get_all_genres():
    genres  = Genre.query.all()
    genre_schema = GenreSchema()
    genres =[genre_schema.dump(genre) for genre in genres]
    return genres

def create_new_genre(name):
    genre = Genre(name=name)
    db.session.add(genre)

    if db.session.commit():
        return genre
    return None 

def get_all_products():
    products = Product.query.all()
    product_schema = ProductSchema()
    products=[product_schema.dump(product) for product in products]
    return products
