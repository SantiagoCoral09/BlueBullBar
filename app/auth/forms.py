from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from flask_babel import _

class RegistroForm(FlaskForm):
    nombre = StringField(_('Name'), validators=[DataRequired(_("You must enter a correct name")), Regexp(r'^[a-zA-Z\s]+$', message=_('Enter a valid name without numbers.'))])
    celular = StringField(_('Phone'), validators=[DataRequired(_("Enter a cell phone number")), Regexp(r'^\d+$', message=_('Enter a valid cell phone number without letters.'))])
    correo = StringField(_('Email'), validators=[DataRequired(_("Enter your e-mail")), Email()])
    password = PasswordField(_('Password'), validators=[DataRequired(_("Enter your password, minimum 6 characters")), Length(min=6, message=_("Must be at least 6 characters"))])
    password_conf = PasswordField(_('Confirm Password'), validators=[DataRequired(_("Enter your password again")), Length(min=6, message=_("Must be at least 6 characters"))])
    submit_registro = SubmitField(_('Sign up now'))

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(_("Enter the email you have registered")), Email()])
    password_l = PasswordField(_('Password'), validators=[DataRequired(_("Enter your password, minimum 6 characters")), Length(min=6, message=_("Must be at least 6 characters"))])
    submit_login = SubmitField(_('Sign in'))