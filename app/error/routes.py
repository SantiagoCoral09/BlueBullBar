from flask import render_template
from . import error_bp

# Manejar el error 400 (Solicitud incorrecta)
@error_bp.app_errorhandler(400)
def bad_request(error):
    return render_template("error.html", error="Solicitud incorrecta", codigo='400'), 400

# Manejar el error 404 (Página no encontrada)
@error_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada", codigo='404'), 404

# Manejar el error 405 (Método no permitido)
@error_bp.app_errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", error="Método no permitido. Revise la solicitud", codigo='405'), 405

# Manejar el error 500 (Error interno del servidor)
@error_bp.app_errorhandler(500)
def internal_error(error):
    return render_template("error.html", error="Error interno del servidor", codigo='500'), 500
