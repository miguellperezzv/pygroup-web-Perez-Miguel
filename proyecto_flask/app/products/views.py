from http import HTTPStatus
from flask import Blueprint,  Response, request 
from app.products.models import get_all_genres, create_new_genre , get_all_products


products = Blueprint('products', __name__, url_prefix = '/products')

RESPONSE_BODY = {
    "message": "",
    "data" : [],
    "errors":[],
    "metadata": []
}


@products.route('/<string:name>', methods=['GET'])
def index(name):
    """DOCUMENTACION
        params: request
        return: response 200, si el nombre es diferente a pygroup
                        400, si el nombre es pygroup
    """

    if name=='pygroup':
        return b'ERROR! No se puede usar el nombre Pygroup' , 400 
    
    return "Felicitaciones! Trabajo exitoso {}".format(name)


@products.route('/genres')
def get_genres():

    genres = get_all_genres()

    RESPONSE_BODY["message"]="Ok"
    RESPONSE_BODY["data"]= genres

    return RESPONSE_BODY, 200

@products.route('"/add-genre', methods=['POST'])
def create_genre():

    if request.method == "POST":
        data =  request.json
        genre = create_new_genre(data["name"])

        RESPONSE_BODY["message"] = "Genero agregado!!!"
        return RESPONSE_BODY, 201


@products.route('/')
def get_products():
    """
    """
    prods = get_all_products()
    RESPONSE_BODY["message"]="Ok"
    RESPONSE_BODY["data"]= prods

    return RESPONSE_BODY, 200
