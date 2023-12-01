from app.services.menu_service import obtener_por_id
class ItemCart:
    def __init__(self, item_id, cantidad, precio_cantidad):
        self.item_id = item_id #id del item del menu
        self.cantidad = cantidad #cantidad del producto
        self.precio_cantidad = precio_cantidad #precio del producto x cantidad


    def __str__(self):
        return f"Id: {self.item_id}, cantidad: {self.cantidad}, precio: {self.precio_cantidad}"

class Cart:
    def __init__(self):
        self.items = []
    
    def add_item(self, item_nuevo):
        """Añade un artículo al carrito"""
        for item in self.items:
            if item.item_id == item_nuevo.item_id:
                item.cantidad += item_nuevo.cantidad
                item.precio_cantidad+=item_nuevo.precio_cantidad
                return

        self.items.append(item_nuevo)
        print('Asi queda el carrito')
        print(self.items)

    def editar_item(self, item_id, nuevo_precio, nueva_cantidad):
        """Actualiza un artículo del carrito"""
        for item in self.items:
            if item.item_id == item_id:
                item.cantidad=nueva_cantidad
                item.precio_cantidad=nuevo_precio
                return
        raise ValueError(f"El artículo con ID {item_id} no se encontró en el carrito.")


    def remove_item(self, item_id):
        """Elimina un artículo del carrito"""
        for item in self.items:
            print(item)
        print(f'id:{item_id}, tipo {type(item_id)}')
        for item in self.items:
            if item.item_id == item_id:
                print('Encontre el item')
                self.items.remove(item)
                return
        raise ValueError(f"El artículo con ID {item_id} no se encontró en el carrito.")


    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.precio_cantidad
        return total
    
    def total_items(self):
        total=0
        for item in self.items:
            total+=item.cantidad
        return total
    
    def obtener_items_carrito(self):
        # Recorre los elementos del carrito y obtén detalles completos del producto
        items_with_details = []
        for item in self.items:
            # Lógica para obtener detalles completos del producto desde la base de datos
            detalles_producto = obtener_por_id(item.item_id)
            items_with_details.append({
                'id': item.item_id,
                'cantidad': item.cantidad,
                'precio': item.precio_cantidad,
                'nombre': detalles_producto.nombre,
                'precio_unidad': detalles_producto.precio,
                'descripcion': detalles_producto.descripcion,
                'imagen': detalles_producto.imagen,
                'categoria':detalles_producto.categoria
            })
        return items_with_details
    
    def __str__(self):
        cadena = ''
        for item in self.items:
            cadena += str(item) + '\n'
        return cadena
    
    def to_dict(self):
        return {
            'items': [
                {
                    'item_id': item.item_id,
                    'cantidad': item.cantidad,
                    'precio_cantidad': item.precio_cantidad
                }
                for item in self.items
            ]
        }

    @classmethod
    def from_dict(cls, data):
        cart = cls()
        for item_data in data.get('items', []):
            item = ItemCart(
                item_data['item_id'],
                item_data['cantidad'],
                item_data['precio_cantidad']
            )
            cart.items.append(item)
        return cart

# cart=Cart()
