import sqlite3
from flask import current_app
from app.models.menu import MenuItem

def obtener_por_categoria(categoria):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Menu WHERE categoria = ?", (categoria,))
    # items = cursor.fetchall()

    # crea una lista de objetos MenuItem a partir de las filas obtenidas de la base de datos
    items = [MenuItem(*row) for row in cursor.fetchall()]

    conn.close()
    return items

def obtener_por_id(id):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Menu WHERE id = ?", (id,))
    # items = cursor.fetchall()

    # fetchone() devuelve una sola tupla o None si no hay resultados
    row = cursor.fetchone()
    if row:
        # crea un objeto MenuItem a partir de la fila obtenida de la base de datos
        item = MenuItem(*row)
    else:
        item = None

    conn.close()
    return item
