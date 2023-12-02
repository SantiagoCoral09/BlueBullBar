from flask import abort, render_template, session

from app.services.usuario_service import obtener_por_email
from . import inicio_bp
from app.models.cart import Cart
from app.services.menu_service import obtener_por_categoria, obtener_por_id
from app.services.cart import obtener_carrito

@inicio_bp.route('/')
def home():
    """Página Inicio"""
    # obtener el carrito en la sesión
    cart=obtener_carrito()

    menu=obtener_por_categoria('Entrada')

    usuario=None
    if 'email' in session:
        # Obtener el id del usuario mediante el email
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)

    return render_template('inicio.html',usuario=usuario, categoria='Platos de Entrada',menu=menu,total_items=cart.total_items())

@inicio_bp.route('/categoria/<categoria>')
def platos_por_categoria(categoria):
    """Página Inicio"""
    menu = obtener_por_categoria(categoria)
    if categoria=='Entrada':
        cat='Platos de Entrada'
    elif categoria=='Principal':
        cat='Platos Principales'
    elif categoria=='Compartir':
        cat='Platos para Compartir'
    elif categoria=='Postre':
        cat='Postres'
    elif categoria=='Bebida':
        cat='Bebidas'
    else:
        abort(404)
    
    # Obtener el id del usuario mediante el email
    usuario=None
    if 'email' in session:
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)
    cart=obtener_carrito()
    return render_template('inicio.html',usuario=usuario,categoria=cat,menu=menu, total_items=cart.total_items())
    
    
@inicio_bp.route('/detalles/<id>')
def detalles(id):
    try:
        """Detalle del Plato"""
        id=int(id)
        item_menu=obtener_por_id(id)
        print(item_menu)

        cart=obtener_carrito()

        usuario=None
        if 'email' in session:
            email_usuario=session['email']
            usuario=obtener_por_email(email_usuario)

        return render_template('detalles.html', usuario=usuario, item_menu=item_menu, total_items=cart.total_items())
    except:
        abort(400)