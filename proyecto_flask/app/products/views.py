import sys
from http import HTTPStatus

from flask import Blueprint, Response, request, render_template, redirect, \
    url_for

from app.products.forms import (CreateGenreForm, CreateProductForm, CreateArtistForm, CreateReleaseForm)
from app.products.models import(
    get_all_genres,
    create_new_genre,
    create_new_product,
    create_new_artist,
    create_new_release,
    get_all_products,
    get_product_by_id,
    get_all_releases,
    get_all_artists,
)

products = Blueprint('products', __name__, url_prefix = '/products')
releases = Blueprint('releases', __name__, url_prefix = '/releases')

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
    return render_template('genre_success.html')

@releases.route('/succcess')
def success():
    return render_template('release_success.html')


@products.route('/create-genre-form', methods=["GET", 'POST'])
def create_genre_form():
    form_genre = CreateGenreForm()

    if request.method == 'POST' and form_genre.validate():
        create_new_genre(name=form_genre.name.data)
        return redirect(url_for('products.success'))

    return render_template('create_genre_form.html', form=form_genre)

@products.route('/add_genre_old', methods=['GET','POST'])
def create_genre_old():
    if request.method == "POST":
        RESPONSE_BODY["message"] = "Se agregó el género {} exitosamente".format(request.form["name"])
        status_code= HTTPStatus.CREATED
        return RESPONSE_BODY, 200
    return render_template("form_genre_old.html")

@products.route("/register-product-stock/<int:id>", methods=["PUT", "POST"])
def register_product_refund_in_stock():

    # TODO Complete this view to update stock for product when a register for
    # this products exists. If not create the new register in DB

    status_code = HTTPStatus.CREATED
    if request.method == "PUT":
        RESPONSE_BODY["message"] = \
            "Stock for this product were updated successfully!"
        status_code = HTTPStatus.OK
    elif request.method == "POST":
        RESPONSE_BODY["message"] = \
            "Stock for this product were created successfully!"
        pass
    else:
        RESPONSE_BODY["message"] = "Method not Allowed"
        status_code = HTTPStatus.METHOD_NOT_ALLOWED

@products.route('/show-catalog', methods=['GET','POST'])
def show_products_catalog():
    #COnsultar la BD y extraer todos los productos disponibles
    products = get_all_products()
    #print(products)
    my_info = {"products" : products, "pygroup": "Pygroup 25 Nov", "miguel": 2020}
    return render_template('catalogo.html', my_info=my_info) ##cuando haga referencia en la plantilla será desde my_info

    #Enviar la info en una variable de contexto
    #renderizar la plantilla de html e insertar los datos de la v de contexto


#Crear un formulario regular y un formulario con Flask-WTF 
# (Utilizando validadores) para la creación de un producto en la tienda.


#formulario con FlaskWTF
@products.route('/nuevo-producto', methods=['GET', 'POST'])
def create_product_form():
    form_product = CreateProductForm()

    if request.method == 'POST' and form_product.validate():
        
        create_new_product(name=form_genre.name.data,price=form_product.price.data, genre_id=form_product.genre.data, image=form_product.image.data) 
        return redirect(url_for('products.success'))
 
    return render_template('create_product_form.html', form=form_product)


#formulario regular
@products.route('/nuevo-producto-old', methods=['GET', 'POST'])
def create_product_old():
    if request.method == "POST":
        RESPONSE_BODY["message"] = "Se agregó el producto {} exitosamente".format(request.form["name"])
        status_code= HTTPStatus.CREATED
        return RESPONSE_BODY, 200
    return render_template("create_product_old.html")


@products.route('/temp')
def temp():
    tempValue = "hola, buenos días"
    return render_template("child.html", myVar = tempValue)

@products.route('/create-artist', methods=["GET", 'POST'])
def create_artist_form():
    form_artist = CreateArtistForm()
    if request.method == 'POST' and form_artist.validate():
        
        create_new_artist(name = form_artist.name.data, description=form_artist.description.data) 
        return redirect(url_for('products.success'))
 
    return render_template('create_artist_form.html', form=form_artist)


@releases.route('/new-release', methods=['GET', 'POST'])
def create_release_form():
    form_release = CreateReleaseForm()

    #if request.method == 'POST' and form_release.validate():
    if request.method == 'POST':
        #release_date = datetime.strptime(form_release_date.data, '%d, %m, %Y')
        release_date = form_release.release_date.data
        create_new_release(artist_id=form_release.artist_id.data, name=form_release.name.data, genre_id=form_release.genre_id.data, release_date=release_date, image=form_release.image.data) 
        print("Producto añadido exitosamente!!!")
        return redirect(url_for('release.success'))

    print("error en agregar release!!!")
    return render_template('create_release_form.html', form=form_release)

@releases.route('/show-catalog', methods=['GET','POST'])
def show_releases_catalog():
    #COnsultar la BD y extraer todos los productos disponibles
    releases = get_all_releases()
    artists = get_all_artists() 
    #print(products)
    my_info = {"releases" : releases, "artists" : artists,  "pygroup": "Pygroup 25 Nov", "miguel": 2020}
    return render_template('catalogo.html', my_info=my_info) ##cuando haga referencia en la plantilla será desde my_info

    #Enviar la info en una variable de contexto
    #renderizar la plantilla de html e insertar los datos de la v de contexto
