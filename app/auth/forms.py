from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class RegistroForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired("Debe ingresar un nombre correcto"), Regexp(r'^[a-zA-Z\s]+$', message='Ingresa un nombre válido sin números.')])
    celular = StringField('Celular', validators=[DataRequired("Ingrese un número de celular"), Regexp(r'^\d+$', message='Ingresa un número de celular válido sin letras.')])
    correo = StringField('Correo Electrónico', validators=[DataRequired("Ingrese su correo electrónico"), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired("Digite su contraseña, mínimo 6 caracteres"), Length(min=6, message="Debe tener mínimo 6 caracteres")])
    submit_registro = SubmitField('Registrarse')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Ingrese el correo que tenga registrado"), Email()])
    password_l = PasswordField('Password', validators=[DataRequired("Digite la contraseña correcta, mínimo 6 caracteres"), Length(min=6, message="Debe tener mínimo 6 caracteres")])
    submit_login = SubmitField('Ingresar')