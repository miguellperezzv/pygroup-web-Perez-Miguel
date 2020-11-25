import sys
from http import HTTPStatus

from flask import Blueprint, Response, request, render_template, redirect, \
    url_for

from app.products.forms import CreateGenreForm
from app.products.models import(
    get_all_genres,
    create_new_genre,
    get_all_products,
    get_product_by_id,
)

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
    RESPONSE_BODY["message"]="Ok. Products list"
    RESPONSE_BODY["data"]= prods

    return RESPONSE_BODY, 200

@products.route('/<int:id>')
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"]=product
    return RESPONSE_BODY, 200
#
#@products.route("/add-product", methods=['POST'])
#def create_product():
#    if request.method == "POST":
#        data = request.json
#        return create_new_product(data["name"], data["price"], data["weight"], data["genre_id"]), 400



@products.route('/succcess')
def success():
    return render_template('category_success.html')

@products.route('/create-genre-form', methods=["GET", 'POST'])
def create_genre_form():
    form_genre = CreateGenreForm()

    if request.method == 'POST' and form_genre.validate():
        create_new_genre(name=form_genre.name.data)
        return redirect(url_form('products.successh'))

    return render_template('create_genre_form.html', form=form_genre)

@products.route('/add_genre_old', methods=['GET','POST'])
def create_genre_old():
    if request.method == "POST":
        RESPONSE_BODY["message"] = "Se agregó el género {} exitosamente".format(request.form["name"])
        status_code= HTTPStatus.CREATED
        return RESPONSE_BODY, 200
    return render_template("form_genre_old.html")