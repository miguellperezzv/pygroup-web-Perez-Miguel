from flask import Blueprint,  Response, request 



prueba = Blueprint('prueba', __name__, url_prefix = '/prueba')

@prueba.route('/<string:name>', methods=['GET'])
def index(name):
    """DOCUMENTACION
        params: request
        return: response 200, si el nombre es diferente a pygroup
                        400, si el nombre es pygroup
    """

    if name=='pygroup':
        return b'ERROR! No se puede usar el nombre Pygroup' , 400 
    
    return "Felicitaciones! Trabajo exitoso {}".format(name)

""" 
        Render Template
        
        este resuelve el problema de no necesariamente retornar un string para una vista.
        Para renderizar una plantilla creada con Jinja2 simplemente se hace uso del método render_template(). 
        A este método debemos se pasa el nombre de nuestra plantilla y las variables necesarias para su renderizado como parámetros clave-valor.
        
        Flask buscará las plantillas en el directorio templates de nuestro proyecto. 
        En el sistema de ficheros, este directorio se debe encontrar en el mismo nivel en el que hayamos definido nuestra aplicación.
        
        El asepcto de las plantillas es similar  a una página html estática con la excepción de  los caracteres {% y %}. 
        Dentro de las llaves se usan los parámetros que se pasaron al método render_template(). 
        El resultado de ello es que durante el renderizado se sustituirán las llaves por el valor de los parámetros que reciba la plantilla. 
        De este modo podemos generar contenido dinámico en nuestras páginas.
        
        Referencias: J2LOGO. Tutorial Flask – Lección 2: Uso de plantillas para las páginas HTML. [Consultado 04/11/2020] Tomado de: https://j2logo.com/tutorial-flask-leccion-2-plantillas/ . 
        
"""
