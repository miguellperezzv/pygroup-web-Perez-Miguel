from flask import Flask , Response



app  = Flask(__name__)



from products import views 
from products.views import prueba
app.register_blueprint(prueba)
#app.register_blueprint(prod)

if __name__== "__main__":
    app.run(debug=True)