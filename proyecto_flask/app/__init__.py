from flask import Flask , Response

from app.db import db, ma 
from conf.config import DevelopmentConfig
#from app.products import views 
from app.products.views import products
from app.products.views import releases
from flask_wtf import CSRFProtect
from flask_migrate import Migrate

ACTIVE_ENDPOINTS = [('/products',products), ('/releases',releases) ]
#ACTIVE_ENDPOINTS = [('/releases',releases)]

def create_app(config=DevelopmentConfig):
    app  = Flask(__name__)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    app.config.from_object(config)
    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)

    with app.app_context():   #el contexto es la DB, el serializable 
        db.create_all()
    
    for url,  blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)
    return app





#app.register_blueprint(products)
#app.register_blueprint(prod)

if __name__== "__main__":
    app_flask =  create_app()
    app_flask.run()
    