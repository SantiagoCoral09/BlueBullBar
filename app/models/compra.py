class Compra:
    def __init__(self, id, id_usuario, fecha_compra, total_compra, metodo_pago):
        self.id = id
        self.id_usuario = id_usuario
        self.fecha_compra = fecha_compra
        self.total_compra = total_compra
        self.metodo_pago = metodo_pago
        # self.direccion = direccion
        # self.items = []

    
class ItemCompra:
    def __init__(self, id, id_compra, item_id, cantidad, precio_cantidad):
        self.id = id
        self.id_compra = id_compra
        self.item_id = item_id #id del item del menu
        self.cantidad = cantidad #cantidad del producto
        self.precio_cantidad = precio_cantidad #precio del producto x cantidad


    def __str__(self):
        return f"Id: {self.item_id}, cantidad: {self.cantidad}, precio: {self.precio_cantidad}"

    
    