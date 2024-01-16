from flask import Flask, redirect, request, session, url_for
from .inicio import inicio_bp
from .auth import auth_bp
from .cart import cart_bp
from .compra import compra_bp
from .error import error_bp
from .admin import admin_bp
from .config.config import DevelopmentMode, ProductionMode
from flask_babel import Babel,_,gettext

app = Flask(__name__)
# app.config.from_object(DevelopmentMode)
# Cuando se vaya a desplegar se pasa a ProductionMode
app.config.from_object(DevelopmentMode)

babel = Babel(app)

app.config['LANGUAGES'] = ['en', 'es']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'

def get_locale():
    # print('Obteniendo idioma')
    # print(session.get('language',request.accept_languages.best_match(app.config['LANGUAGES'])))
    return session.get('language', request.accept_languages.best_match(app.config['LANGUAGES']))


@app.route('/set_language/<language>')
def set_language(language):
    if language in app.config['LANGUAGES']:
        session['language'] = language
        # print(f"Lenguaje en sesion: {session['language']}")
        # print(gettext('Hello, World!'))
    # else:
    #     print(f"{language} no está en el config")
    return redirect(request.referrer or url_for('inicio.home'))

babel.init_app(app, locale_selector=get_locale)

app.register_blueprint(inicio_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(compra_bp)
app.register_blueprint(error_bp)
app.register_blueprint(admin_bp)

