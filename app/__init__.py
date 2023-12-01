from flask import Flask, redirect, render_template, url_for
from .inicio import inicio_bp
from .auth import auth_bp
from .cart import cart_bp
from .compra import compra_bp
from .error import error_bp

app = Flask(__name__)
app.secret_key='clave_secreta'
app.config.from_pyfile('config/configuracion.cfg')

app.register_blueprint(inicio_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(error_bp)


@app.route('/trigger-500')
def trigger_500():
    # Lanzar una excepción para provocar un error 500
    raise Exception("Este es un error interno del servidor")