from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_babel import _
class DatosCompraForm(FlaskForm):
    metodo_pago=SelectField(_("Payment Method"), choices=[ ("Efectivo", _("Cash/Efectivo")),
        ("PSE", "PSE"),
        ("Tarjeta", _("Card/Tarjeta"))], validators=[DataRequired(message="Select a payment method")])
    submit_compra=SubmitField("Complete Purchase")
