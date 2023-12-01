from flask import Blueprint

compra_bp = Blueprint('compra', __name__, template_folder='templates', static_folder='static')
from . import routes