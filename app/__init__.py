from flask import Flask
from .inicio import inicio_bp
from .auth import auth_bp
from .cart import cart_bp
from .compra import compra_bp
from .error import error_bp
from .admin import admin_bp
from .config.config import DevelopmentMode, ProductionMode

app = Flask(__name__)
app.config.from_object(DevelopmentMode)
# Cuando se vaya a desplegar se pasa a ProductionMode
# app.config.from_object(ProductionMode)


app.register_blueprint(inicio_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(error_bp)
app.register_blueprint(admin_bp)

