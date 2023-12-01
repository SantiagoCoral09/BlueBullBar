from flask import render_template
from . import error_bp

# Manejar el error 404 (Página no encontrada)
@error_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada...", codigo='404'), 404

# Manejar el error 500 (Error interno del servidor)
@error_bp.app_errorhandler(500)
def internal_error(error):
    return render_template("error.html", error="Página no encontrada...", codigo='500'), 500

