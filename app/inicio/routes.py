from flask import abort, render_template, request, session

from app.services.usuario_service import obtener_por_email
from . import inicio_bp
from app.models.cart import Cart
from app.services.menu_service import obtener_por_categoria, obtener_por_id, PER_PAGE, obtener_total_menu
from app.services.cart import obtener_carrito
from flask_paginate import Pagination

@inicio_bp.route('/')
def home():
    """Página Inicio"""
    # obtener el carrito en la sesión
    cart=obtener_carrito()

    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * PER_PAGE
    
    menu=obtener_por_categoria('Entrada',offset)
    total_items =obtener_total_menu('Entrada')
    pagination = Pagination(page=page, total=total_items, per_page=PER_PAGE, bs_version=4, 
        display_msg="Mostrando {start} - {end} de {total} registros en total")
    
    usuario=None
    if 'email' in session:
        # Obtener el id del usuario mediante el email
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)

    return render_template('inicio.html',usuario=usuario, categoria='Platos de Entrada',menu=menu,total_items_cart=cart.total_items(), pagination=pagination)

@inicio_bp.route('/categoria/<categoria>')
def platos_por_categoria(categoria):
    """Página Inicio"""

    page = request.args.get('page', 1, type=int)
    offset = (page - 1) * PER_PAGE
    
    menu=obtener_por_categoria(categoria,offset)
    total_items =obtener_total_menu(categoria)
    pagination = Pagination(page=page, total=total_items, per_page=PER_PAGE, bs_version=4, 
        display_msg="Mostrando {start} - {end} de {total} registros en total")
    
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
    return render_template('inicio.html',usuario=usuario,categoria=cat,menu=menu, total_items_cart=cart.total_items(), pagination=pagination)
    
    
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

        return render_template('detalles.html', usuario=usuario, item_menu=item_menu, total_items_cart=cart.total_items())
    except:
        abort(400)