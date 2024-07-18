import os
from flask import Flask

#FUNCION QUE EJECUTARA LA APLICACION
def create_app():
    #CREANDO EL OBJETO FLASK
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('KEY')
    from .views import views
    app.register_blueprint(views)
    return app