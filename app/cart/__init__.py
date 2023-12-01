from flask import Blueprint

cart_bp = Blueprint('cart', __name__, template_folder='templates', static_folder='static')
from . import routes