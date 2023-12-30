import sqlite3
from flask import current_app
from app.models.usuario import Usuario

def obtener_usuarios():
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuario",)
    # usuarios = cursor.fetchall()

    # crea una lista de objetos Usuario a partir de las filas obtenidas de la base de datos
    usuarios = [Usuario(*row) for row in cursor.fetchall()]
    print(usuarios)
    conn.close()
    return usuarios

def obtener_por_email(email):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuario WHERE email = ?", (email,))
    # usuarios = cursor.fetchall()

    row = cursor.fetchone()
    print('resultado obtenido')
    print(row)
    if row:
        print(f"{row[0]}-{row[3]}-{row[5]}")

        # crea un objeto Usuario a partir de la fila obtenida de la base de datos
        usuario = Usuario(id=row[0],nombres=row[1],celular=row[2],email=row[3],password=row[4],tipo_usuario=row[5])
    else:
        usuario=None
    print(f"El usuario obtenido::: {usuario}")
    conn.close()
    return usuario


def obtener_por_id(id):
    db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Usuario WHERE id = ?", (id,))
    # usuarios = cursor.fetchall()

    # fetchone() devuelve una sola tupla o None si no hay resultados
    row = cursor.fetchone()
    if row:
        # crea un objeto Usuario a partir de la fila obtenida de la base de datos
        usuario = Usuario(*row)
    else:
        usuario = None
    print(usuario)
    conn.close()
    return usuario

def agregar_usuario(usuario:Usuario):
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///', '')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        sql = '''INSERT INTO Usuario (nombres, celular, email, password, tipo_usuario) VALUES(?,?,?,?,?);'''
        params = (usuario.nombres, usuario.celular, usuario.email, usuario.password, usuario.tipo_usuario)
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

        return True  # Si la inserción fue exitosa
    except Exception as e:
        print(f"Error al agregar usuario: {e}")
        return False
    
def actualizarUsuario(usuario: Usuario):
    try:
        db_path = current_app.config['DATABASE_URI'].replace('sqlite:///','')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        # Actualizamos el registro en la tabla Usuario
        sql = """UPDATE Usuario SET nombres = ?, celular = ?, email = ?, password=?, tipo_usuario = ? WHERE id = ?;"""
        params = (usuario.nombres, usuario.celular, usuario.email, usuario.password, 
                  usuario.tipo_usuario, usuario.id)
        cursor.execute(sql,params)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return False
    