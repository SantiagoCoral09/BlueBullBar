from flask import flash, render_template, request, redirect, url_for, session
from app.compra.forms import DatosCompraForm
from app.models.compra import Compra, ItemCompra
from app.models.cart import Cart
from app.services.compra_service import agregar_compra, agregar_item_compra
from app.services.usuario_service import obtener_por_email
from app.services.cart import obtener_carrito
from datetime import datetime
from . import compra_bp

@compra_bp.route('/realizar_compra', methods=["GET", "POST"])
def realizar_compra():
    cart = obtener_carrito()
    carrito = cart.obtener_items_carrito()
    total = cart.calcular_total() #valor total a pagar
    cantidad_items=carrito.__len__()
    print(f"cantidad items: {cantidad_items}")
    if 'email' in session:
        # Obtener el id del usuario mediante el email
        email_usuario=session['email']
        usuario=obtener_por_email(email_usuario)
        
        form_compra = DatosCompraForm(request.form)
        if form_compra.submit_compra.data:
            if form_compra.validate_on_submit():
            
                print(f"El usuario en sesion: {email_usuario}::::{usuario}")
                id_usuario=usuario.id
                fecha_compra=datetime.now()
                metodo_pago=form_compra.metodo_pago.data
                nueva_compra=Compra(
                    id=None,
                    id_usuario=id_usuario,
                    fecha_compra=fecha_compra,
                    total_compra=total,
                    metodo_pago=metodo_pago
                )
                # Guarda la compra en la base de datos
                try:
                    exito,id_compra = agregar_compra(nueva_compra)
                    if exito==True:
                        for item in carrito:
                            print(f"Item:: {item['id']}")
                            item_compra=ItemCompra(id=None,id_compra=id_compra,item_id=item['id'],cantidad=item['cantidad'],precio_cantidad=item['precio'])
                            if agregar_item_compra(item_compra):
                                cart.remove_item(item['id'])
                                # Guardar el carrito en la sesión
                                session['cart'] = cart.to_dict()
                                cart = obtener_carrito()
                                carrito = cart.obtener_items_carrito()
                                total = cart.calcular_total() #valor total a pagar
                        print(f"cantidad items ahhora es: {carrito.__len__()}")
                        if carrito.__len__()==0:
                            flash('La compra se ha realizado con éxito!','success')
                            return redirect(url_for("inicio.home"))
                        
                    else:
                        flash(f"Error al guardar la compra",'warning')
                except Exception as e:
                    flash(f"Se produjo el error: {e}",'danger')
            else:
                flash("Error de validación del formluario",'warning')

        return render_template('realizar_compra.html', usuario=usuario, form=form_compra, carrito=carrito, total=total, total_items_cart=cart.total_items())
    else:
        return redirect(url_for("auth.login_registro"))