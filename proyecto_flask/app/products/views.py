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