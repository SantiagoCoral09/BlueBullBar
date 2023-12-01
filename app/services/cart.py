
from flask import session
from app.models.cart import Cart


def obtener_carrito():
    """Obtiene el carrito de la sesión o crea uno nuevo si no existe."""
    if 'cart' not in session:
        # Si no está en la sesión, crear uno nuevo
        cart = Cart()
        session['cart'] = cart.to_dict()
    else:
        # Si ya está en la sesión, obtenerlo y convertirlo a una instancia de Cart
        cart = Cart.from_dict(session['cart'])
    return cart