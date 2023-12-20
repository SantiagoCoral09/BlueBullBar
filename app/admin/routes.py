from flask import redirect, render_template, request, session, url_for
from app.admin import admin_bp
from app.services.menu_service import  PER_PAGE, obtener_menu_paginate, obtener_total_menu
from app.services.usuario_service import obtener_por_email
from flask_paginate import Pagination

@admin_bp.route('/panel_control')
def panel_control():
    usuario=None
    if 'email' in session and session['tipo_usuario']=='admin':
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)

        page = request.args.get('page', 1, type=int)
        offset = (page - 1) * PER_PAGE


        items_menu=obtener_menu_paginate(offset)
        total_items =obtener_total_menu('all')
        pagination = Pagination(page=page, total=total_items, per_page=PER_PAGE, bs_version=4, 
        display_msg="Mostrando {start} - {end} de {total} registros en total")

        return render_template('panel_control.html', usuario=usuario, items_menu=items_menu, total=total_items, pagination=pagination)
    else:
        return redirect(url_for('inicio.home'))
