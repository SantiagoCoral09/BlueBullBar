from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

# Importar las rutas después de definir el blueprint para evitar ciclos de importación
from . import routes
