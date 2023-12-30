from flask import flash, render_template, request, redirect, url_for, session

from app.services.usuario_service import obtener_por_email
from . import cart_bp
from app.models.cart import ItemCart
from app.services.menu_service import obtener_por_id
from app.services.cart import obtener_carrito
from flask_babel import _

@cart_bp.route('/agregar_item/<id_item>', methods=['POST'])
def agregar_item(id_item):
    if request.method == 'POST':
        cantidad = int(request.form['cantidad'])
        precio=float(request.form['precio_x_cantidad'])
        if cantidad > 0:       
            #  Buscar los atributos del producto para guardarlos en el ItemCart
            cart=obtener_carrito()
            cart.add_item(ItemCart(id_item, cantidad, precio))
            print(f'cantidad:{cantidad}, precio:{precio}')
            print(f'id: {id_item}')

            # Guardar el carrito en la sesión
            session['cart'] = cart.to_dict()

            # Página de inicio
            print(cart.obtener_items_carrito())

            mensaje=_("Added to cart")
            flash(f"{mensaje} '{obtener_por_id(id_item).nombre}'",'success')
            return redirect(url_for('inicio.home'))
        else:
            flash(_("Choose a correct quantity"),'warning')
            return redirect(url_for('inicio.detalles', id=id_item))
    else:
        flash(_("Internal error"),'danger')
        return redirect(url_for('inicio.home'))

@cart_bp.route('/mostrar_carrito')
def mostrar_carrito():
    cart = obtener_carrito()
    carrito = cart.obtener_items_carrito()
    total = cart.calcular_total()

    usuario=None
    if 'email' in session:
    # Obtener el id del usuario mediante el email para mostrar sus datos en la pagina
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)

    return render_template("carrito.html", usuario=usuario, carrito=carrito, total=total, total_items_cart=cart.total_items())

@cart_bp.route('/editar_item/<id>', methods=['POST'])
def editar_item(id):
    if request.method == 'POST':
        nueva_cantidad = int(request.form.get(f'cantidad_{id}'))
        nuevo_precio_x_cantidad = float(request.form.get(f'precio_x_cantidad_{id}'))

        print(f'Nueva cantidad: {nueva_cantidad}, Prec*cant: {nuevo_precio_x_cantidad}')
        if nueva_cantidad > 0:
            # Obtener el carrito en sesion para actualizarlo
            cart=obtener_carrito()
            cart.editar_item(id,nuevo_precio_x_cantidad,nueva_cantidad)

            # Guardar el carrito actualizado en la sesión
            session['cart'] = cart.to_dict()

            # Mostrar un mensaje del producto actualizado
            mensaje=_("Updated quantity of")
            flash(f"{mensaje} '{obtener_por_id(id).nombre}'",'success')
        return redirect(url_for('cart.mostrar_carrito'))

@cart_bp.route('/eliminar_item/<id>')
def eliminar_item(id):
    # Eliminar el ítem del carrito 

    # Obtener el carrito en sesion para actualizarlo
    cart=obtener_carrito()
    cart.remove_item(id)

    # Guardar el carrito actualizado en la sesión
    session['cart'] = cart.to_dict()

    
    # Mostrar un mensaje del producto actualizado
    flash(_("Removed from cart: '{name}'").format(name=obtener_por_id(id).nombre), 'warning')
    return redirect(url_for('cart.mostrar_carrito'))