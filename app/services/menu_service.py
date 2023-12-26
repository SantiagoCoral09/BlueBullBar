import sqlite3
from flask import current_app
from app.models.menu import MenuItem


# Numero de items a mostrar en una pagina
PER_PAGE = 5

def obtener_total_menu(opcion):
    """Obtiene la cantidad de items en menu de la base de datos"""
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if opcion=='all':
            # Obtener todos los items del menú
            cursor.execute("SELECT COUNT(*) FROM Menu")
        else:    
            # Obtener solo las Entradillas
            cursor.execute(f"SELECT COUNT(*) FROM Menu where categoria='{opcion}'")

        total_items = cursor.fetchone()[0]
        conn.close()
        return total_items
    except Exception as e:
        print("Error al obtener el menu: ", str(e))
        raise e
    
def obtener_menu_paginate(offset=0):
    """Obtiene el menu de la base de datos"""
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Obtener todos los items del menú
        query = f"SELECT * FROM Menu LIMIT {PER_PAGE} OFFSET {offset}"
        cursor.execute(query)
        # crea una lista de objetos MenuItem a partir de las filas obtenidas de la base de datos
        items = [MenuItem(*row) for row in cursor.fetchall()]
        # items = cursor.fetchall()
        # Cierra la conexión a la BD y devuelve la lista de Items
        conn.close()
        return items
    except Exception as e:
        print("Error al obtener el menu: ", str(e))
        raise e
    

def obtener_por_categoria(categoria,offset=0):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = f"SELECT * FROM Menu WHERE categoria='{categoria}' LIMIT {PER_PAGE} OFFSET {offset}"
    cursor.execute(query)
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

def agregar_item(menuItem:MenuItem):
    try:
        db_path = current_app.config["DATABASE_URI"].replace("sqlite:///","")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Agrega el nuevo elemento en la tabla "Menu"
        cursor.execute("INSERT INTO Menu (nombre,descripcion,precio,categoria,imagen) VALUES(?,?,?,?,?);",
                       (menuItem.nombre,menuItem.descripcion,menuItem.precio,menuItem.categoria,menuItem.imagen))
        # Devuelve el ID del nuevo elemento
        id = cursor.lastrowid
        # Confirma los cambios y cierra la conexión a la BD
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al insertar el item: {e}")
        return False
    
def modificar_item(menuItem:MenuItem):
    try:
        db_path = current_app.config["DATABASE_URI"].replace("sqlite:///","")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Modifica el elemento en la tabla "Menu"
        cursor.execute(f"""UPDATE Menu
        SET nombre='{menuItem.nombre}', descripcion='{menuItem.descripcion}', precio={menuItem.precio}, categoria='{menuItem.categoria}', imagen='{menuItem.imagen}'
        WHERE id={menuItem.id}""")
        
        # Confirma los cambios y cierra la conexión a la BD
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al modificar el item: {e}")
        return False
    
def eliminar_item(item_id):
    """Elimina un elemento por su ID."""
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM Menu WHERE id="{item_id}";')
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al eliminar el item: {e}")
        return False
    
