from app.services.usuario_service import obtener_por_email

def verificar_email(email):
    usuario=obtener_por_email(email)
    if usuario is not None:
        return True
    else:
        return False

def verificar_password(email, password):
    usuario=obtener_por_email(email)
    if usuario is not None:
        if usuario.password == password:
            return True
        else:
            return False
    else:
        return False

