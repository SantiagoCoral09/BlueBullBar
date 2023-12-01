import os
import sqlite3

def consultar_menu():
    # Obtener la ruta absoluta al directorio actual del script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir la ruta absoluta al archivo de la base de datos (asegúrate de que coincide con la ruta usada en create_tables.py)
    db_path = os.path.join(script_dir, '..', 'database', 'bluebullbar.db')
    print(db_path)

    # Conectar a la base de datos
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Realizar consultas, operaciones, etc.

    # Ejemplo de consulta de menú
    cursor.execute("SELECT * FROM Menu")
    filas = cursor.fetchall()

    # Realizar operaciones adicionales si es necesario

    conn.close()

    return filas

consultar_menu()
