from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp
class DatosCompraForm(FlaskForm):
    metodo_pago=SelectField("Método de pago", choices=["Efectivo","PSE","Tarjeta"], validators=[DataRequired(message="Seleccione un método de pago")])
    submit_compra=SubmitField("Finalizar Compra")
