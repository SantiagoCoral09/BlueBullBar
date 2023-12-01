class MenuItem:
    def __init__(self, id, nombre, descripcion, precio, categoria, imagen):
        self.id=id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
        self.imagen=imagen

    
    def __str__(self):
        return f"{self.id}:{self.nombre}"


# menu_entradas=[
#     MenuItem(1,'Nachos Supreme','Nachos cubiertos con queso fundido, guacamole, crema agria, jalapeños y salsa',15000,'entradas','nachos.jpg'),
#     MenuItem(2,'Aros de cebolla','Crujientes aros de cebolla servidos con salsa BBQ',17000,'entradas','aros_cebolla.jpg'),
#     MenuItem(3,'Bruschettas de tomate y albahaca','Pan tostado con tomate fresco, ajo, albahaca y aceite de oliva',12000,'entradas','bruschettas_tomate.jpg'),
# ]

# menu_platos_principales=[
#     MenuItem(4,'Hamburguesa clásica','Carne a la parrilla con queso cheddar, lechuga, tomate y cebolla caramelizada',20000,'platos_principales','hamburguesa.jpg'),
#     MenuItem(5,'Ensalada César con pollo a la parrilla','Lechuga romana, pollo a la parrilla, crotones, queso parmesano y aderezo César',2000,'platos_principales','ensalada_cesar.jpg'),
#     MenuItem(6,'Tacos de camarones','Tacos de camarones a la parrilla con col morada, salsa de cilantro y lima',22000,'platos_principales','tacos_camarones.jpg'),
# ]

# menu_platos_compartir=[
#     MenuItem(7,'Tabla de quesos y embutidos','Variedad de quesos, embutidos, frutos secos y mermeladas',12000,'platos_compartir','tabla_quesos_embutidos.jpg'),
#     MenuItem(8,'Parrillada mixta','Selección de carnes a la parrilla con chorizo, pollo y cerdo, acompañada de papas asadas y vegetales a la parrilla',22000,'platos_compartir','parrillada_mixta.jpg'),
# ]

# menu_postres=[
#     MenuItem(9,'Tarta de chocolate','Deliciosa tarta de chocolate con helado de vainilla.',15000,'postres','tarta_chocolate.jpg'),
#     MenuItem(10,'Coulant de caramelo','Coulant caliente de caramelo con helado de dulce de leche.',12000,'postres','coulant_caramelo.jpg')
# ]

# menu_bebidas=[
#     MenuItem(11,'Cocktails clásicos','Margarita, Mojito, Piña Colada.',5000,'bebidas',''),
#     MenuItem(12,'Cervezas artesanales','Variedad de cervezas locales e internacionales.',7000,'bebidas',''),
#     MenuItem(13,'Vinos y licores','Selección de vinos tintos, blancos y licores.',10000,'bebidas','')
# ]