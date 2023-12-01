import sqlite3
from flask import current_app
from app.models.compra import Compra, ItemCompra

def obtener_compras():
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Compra",)
    # compras = cursor.fetchall()

    # crea una lista de objetos Compra a partir de las filas obtenidas de la base de datos
    compras = [Compra(*row) for row in cursor.fetchall()]
    print(compras)
    conn.close()
    return compras

def obtener_por_id_usuario(id_usuario):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Compra WHERE usuario_id = ?", (id_usuario,))
    # compras = cursor.fetchall()

    row = cursor.fetchone()
    print('resultado obtenido')
    print(row)
    if row:
        # crea un objeto Compra a partir de la fila obtenida de la base de datos
        compra = Compra(
            id=row[0],
            id_usuario=row[1],
            fecha_compra=row[2],
            total_compra=row[3],
            metodo_pago=row[4],
            direccion=row[5]
        )
    else:
        compra = None
    print(compra)
    conn.close()
    return compra


def obtener_por_id(id):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Compra WHERE id = ?", (id,))
    # compras = cursor.fetchall()

    # fetchone() devuelve una sola tupla o None si no hay resultados
    row = cursor.fetchone()
    if row:
        # crea un objeto Compra a partir de la fila obtenida de la base de datos
        compra = Compra(*row)
    else:
        compra = None
    print(compra)
    conn.close()
    return compra

def agregar_compra(compra:Compra):
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = '''INSERT INTO Compras (usuario_id, fecha_compra, total_compra, metodo_pago) VALUES(?,?,?,?);'''
        params = (compra.id_usuario, compra.fecha_compra, compra.total_compra, compra.metodo_pago)
        cursor.execute(sql, params)
        conn.commit()
        # Obtener el ID de la última fila insertada
        compra_id = cursor.lastrowid
        conn.close()

        return True, compra_id  
        # Si la inserción fue exitosa devuelve True y el id de la compra registrada
    except Exception as e:
        print(f"Error al agregar compra: {e}")
        return False, None
    
def agregar_item_compra(item_compra: ItemCompra):
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = '''INSERT INTO Compras_Item (compra_id, item_id, cantidad, subtotal) VALUES(?,?,?,?);'''
        params = (item_compra.id_compra, item_compra.item_id, item_compra.cantidad, item_compra.precio_cantidad)

        cursor.execute(sql, params)
        conn.commit()
        conn.close()
        return True  # Si la inserción fue exitosa
    except Exception as e:
        print(f"Error al agregar item de compra: {e}")
        return False
    