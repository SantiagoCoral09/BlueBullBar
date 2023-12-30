from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import InputRequired, DataRequired
from flask_babel import _

class ProductForm(FlaskForm):
    nombre = StringField(_('Name'), validators=[DataRequired(_('You must enter the product name'))])
    descripcion = TextAreaField(_("Description"), validators=[DataRequired(_('Enter a description'))])
    precio = IntegerField(_('Price'), validators=[DataRequired(_("Enter a price"))])
    categoria = SelectField(_("Select a category"), choices=[('Entrada', _('Entrie')),('Principal',_("Main course")),('Compartir',_("Dish to share")),('Postre',_('Dessert')),('Bebida',_('Drink'))])
    imagen = StringField(_('Enter the URL of the Image'), validators=[DataRequired(_('Enter the URL of the Image'))])
    submit_agregar = SubmitField(_('Save'))