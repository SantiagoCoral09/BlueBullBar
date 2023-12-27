import datetime
import sqlite3
import jwt
from flask import current_app

class Usuario:
    def __init__(self, id, nombres, celular, email, password, tipo_usuario):
        self.id=id
        self.nombres = nombres
        self.celular = celular
        self.email = email
        self.password = password
        self.tipo_usuario=tipo_usuario #admin o public

    def __str__(self):
        return f"User(id={self.id}, email={self.email})"
    
    def get_reset_token(self, expires_sec=1800):
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_sec)
        }
        token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS512')
        return token



    @staticmethod
    def verify_reset_token(token):
        try:
            payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS512'])
            user_id = payload['user_id']
            return obtener_por_id(user_id)
        except jwt.ExpiredSignatureError:
            # Token expirado
            return None
        except jwt.InvalidTokenError:
            # Token inválido
            return None

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