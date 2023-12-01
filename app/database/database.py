import os
import sqlite3

def create_tables():
    # Obtener la ruta absoluta al directorio actual del script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta absoluta al archivo de la base de datos
    db_path = os.path.join(script_dir, 'bluebullbar.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Sentencias SQL para crear las tablas si no existen
    sentencias_sql = """
        CREATE TABLE IF NOT EXISTS Menu (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL,
            imagen TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Usuario (
            id INTEGER PRIMARY KEY,
            nombres TEXT NOT NULL,
            celular TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            tipo_usuario TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS Compras (
            id INTEGER PRIMARY KEY,
            usuario_id INTEGER,
            fecha_compra TEXT NOT NULL,
            total_compra REAL NOT NULL,
            metodo_pago TEXT NOT NULL,
            FOREIGN KEY (usuario_id) REFERENCES Usuario(id)
        );

        CREATE TABLE IF NOT EXISTS Compras_Item (
            id INTEGER PRIMARY KEY,
            compra_id INTEGER,
            item_id INTEGER,
            cantidad INTEGER NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY (compra_id) REFERENCES Compras(id),
            FOREIGN KEY (item_id) REFERENCES Menu(id)
        );

        INSERT INTO Menu (nombre, descripcion, precio, categoria, imagen) VALUES
            ('Nachos Supreme','Nachos cubiertos con queso fundido, guacamole, crema agria, jalapeños y salsa',15000,'Entrada','nachos.jpg'),
            ('Aros de cebolla','Crujientes aros de cebolla servidos con salsa BBQ',17000,'Entrada','aros_cebolla.jpg'),
            ('Bruschettas de tomate y albahaca','Pan tostado con tomate fresco, ajo, albahaca y aceite de oliva',12000,'Entrada','bruschettas_tomate.jpg'),
            ('Hamburguesa clásica','Carne a la parrilla con queso cheddar, lechuga, tomate y cebolla caramelizada',20000,'Principal','hamburguesa.jpg'),
            ('Ensalada César con pollo a la parrilla','Lechuga romana, pollo a la parrilla, crotones, queso parmesano y aderezo César',2000,'Principal','ensalada_cesar.jpg'),
            ('Tacos de camarones','Tacos de camarones a la parrilla con col morada, salsa de cilantro y lima',22000,'Principal','tacos_camarones.jpg'),
            ('Tabla de quesos y embutidos','Variedad de quesos, embutidos, frutos secos y mermeladas',12000,'Compartir','tabla_quesos_embutidos.jpg'),
            ('Parrillada mixta','Selección de carnes a la parrilla con chorizo, pollo y cerdo, acompañada de papas asadas y vegetales a la parrilla',22000,'Compartir','parrillada_mixta.jpg'),
            ('Tarta de chocolate','Deliciosa tarta de chocolate con helado de vainilla.',15000,'Postre','tarta_chocolate.jpg'),
            ('Coulant de caramelo','Coulant caliente de caramelo con helado de dulce de leche.',12000,'Postre','coulant_caramelo.jpg'),
            ('Cocktails clásicos','Margarita, Mojito, Piña Colada.',5000,'Bebida','https://www.gastroactitud.com/wp-content/uploads/2022/08/manhattan-apertura.jpg'),
            ('Cervezas artesanales','Variedad de cervezas locales e internacionales.',7000,'Bebida','https://tienda.cristar.com.co/wp-content/uploads/2023/01/ESTILOS-DE-CERVEZAS.jpg'),
            ('Vinos y licores','Selección de vinos tintos, blancos y licores.',10000,'Bebida','https://cava-alta.com/wp-content/uploads/2020/05/mayor-1.jpg');
    """

    try:
        cursor.executescript(sentencias_sql)
        conn.commit()
        print('Se crearon las tablas...')
    except sqlite3.Error as e:
        print("Error al ejecutar las sentencias SQL:", e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_tables()
