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