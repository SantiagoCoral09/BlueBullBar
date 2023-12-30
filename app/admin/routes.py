from flask import flash, redirect, render_template, request, session, url_for
from app.admin import admin_bp
from app.admin.form import ProductForm
from app.services.menu_service import  PER_PAGE, agregar_item, eliminar_item, modificar_item, obtener_menu_paginate, obtener_por_id, obtener_total_menu
from app.services.usuario_service import obtener_por_email
from flask_paginate import Pagination
from app.models.menu import MenuItem
from flask_babel import _

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
        display_msg=_("Showing {start} - {end} of {total} total records"))

        return render_template('panel_control.html', usuario=usuario, items_menu=items_menu, total=total_items, pagination=pagination)
    else:
        return redirect(url_for('inicio.home'))

@admin_bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    usuario=None
    if 'email' in session and session['tipo_usuario']=='admin':
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)

        form = ProductForm(request.form)
        if form.submit_agregar.data:
            if form.validate_on_submit():
                # Guarda el producto y redirige a la lista de productos
                nuevo_item=MenuItem(id=None,nombre=form.nombre.data, descripcion=form.descripcion.data, precio=form.precio.data, categoria=form.categoria.data, imagen=form.imagen.data)

                try:
                    if agregar_item(nuevo_item):
                        print('Se guardado con exito')
                        flash(_("Saved successfully"),"success")
                        return redirect(url_for('admin.panel_control'))
                    else:
                        print('Error al guardar')
                        flash(_("Error saving item"), "danger")
                except Exception as e:
                    print(f"Se produjo la excepcion: {e}")
                    flash(_('Unknown error'), "warning")
            else:
                flash(_("Incorrect data"),"warning")
                # return render_template("agregar_producto.html",usuario=usuario, form=form)

        return render_template("agregar_producto.html",usuario=usuario, form=form)
    else:
        return redirect(url_for('inicio.home'))
    
@admin_bp.route('/modificar/<item_id>', methods=['GET', 'POST'])
def modificar(item_id):
    usuario=None
    if 'email' in session and session['tipo_usuario']=='admin':
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)
        item=obtener_por_id(item_id)
        print(f"Item con id: {item_id}")
        print(item)
        if request.method == 'POST':
            # Obtén los datos del formulario oculto
            nombre = request.form.get('nombre')
            precio = request.form.get('precio')
            descripcion=request.form.get('descripcion')
            imagen=request.form.get('imagen')
            categoria=request.form.get('categoria')
            item_modificar=MenuItem(id=item_id,nombre=nombre,descripcion=descripcion,precio=precio,categoria=categoria,imagen=imagen)

            try:
                if modificar_item(item_modificar):
                    print('Se guardado con exito')
                    flash(_("Saved successfully!!"),"success")
                    return redirect(url_for('admin.panel_control'))
                else:
                    print('Error al guardar')
                    flash(_("Error saving item"), "danger")
            except Exception as e:
                print(f"Se produjo la excepcion: {e}")
                flash(_("Unknown error"), "warning")


        return redirect(url_for('admin.panel_control'))
    else:
        return redirect(url_for('inicio.home'))
    
@admin_bp.route('/eliminar/<item_id>', methods=['GET', 'POST'])
def eliminar(item_id):
    usuario=None
    if 'email' in session and session['tipo_usuario']=='admin':
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)
        item=obtener_por_id(item_id)
        print(f"Item con id: {item_id}")
        print(item)
        if request.method == 'GET':
            print(item_id)
            if eliminar_item(item_id):
                flash(_("Successful removal"),"success")
            else:  
                flash(_("Could not delete item"),"danger")

        return redirect(url_for('admin.panel_control'))
    else:
        return redirect(url_for('inicio.home'))