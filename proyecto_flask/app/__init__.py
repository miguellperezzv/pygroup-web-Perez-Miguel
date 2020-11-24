from flask import Flask , Response

from db import db, ma 
from config import DevelopmentConfig
from products import views 
from products.views import products
from flask_wtf import CSRFProtect
ACTIVE_ENDPOINTS = [('/products',products)]

def create_app(config=DevelopmentConfig):
    app  = Flask(__name__)
    csrf = CSRFProtect(app)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)

    with app.app_context():   #el contexto es la DB, el serializable 
        db.create_all()
    
    for url,  blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)






#app.register_blueprint(products)
#app.register_blueprint(prod)

if __name__== "__main__":
    app_flask =  create_app()
    app_flask.run()
    