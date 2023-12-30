from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired

class ProductForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired('Debe ingresar el nombre del producto')])
    descripcion = TextAreaField('Descripción', validators=[DataRequired('Ingrese una descripción')])
    precio = IntegerField('Precio', validators=[DataRequired('Ingrese un precio')])
    categoria = SelectField('Seleccione una categoría', choices=[('Entrada', 'Plato de Entrada'),('Principal','Plato principal'),('Compartir','Plato para compartir'),('Postre','Postre'),('Bebida','Bebida')])
    imagen = StringField('Ingrese la url de la Imagen', validators=[DataRequired('Ingrese la url de la imagen')])
    submit_agregar = SubmitField('Registrar')