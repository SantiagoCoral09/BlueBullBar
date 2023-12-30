from flask import current_app, render_template, request, redirect, url_for, session, flash
from app.auth.forms import LoginForm, RegistroForm
from app.config.config import Config, MAIL_USERNAME, mail
from app.models.usuario import Usuario
from app.services.cart import obtener_carrito
from app.services.usuario_service import actualizarUsuario, agregar_usuario, obtener_por_email
from . import auth_bp
from flask_mail import Mail, Message
from flask_babel import _



@auth_bp.route('/login_registro', methods=["GET", "POST"])
def login_registro():
    # print(f'USERNAME: {MAIL_USERNAME}')
    if 'email' in session:
        if session['tipo_usuario']=='admin':
            return redirect(url_for('admin.panel_control'))
        return redirect(url_for('inicio.home'))
    cart = obtener_carrito()
    form_registro = RegistroForm(request.form)
    form_login = LoginForm(request.form)


    if form_registro.submit_registro.data and form_registro.validate_on_submit():
        # Llega el formulario de registro
        correo_registro=form_registro.correo.data
        existe_usuario=obtener_por_email(correo_registro)
        if existe_usuario:
            print('Correo ya existe')
            flash(_('The email is already registered. Sign in if you already have an account.'),'warning')
            return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())
        else:
                    # Si el correo no está registrado, procede con el registro
            nuevo_usuario = Usuario(
                id=None,
                nombres=form_registro.nombre.data,
                celular=form_registro.celular.data,
                email=form_registro.correo.data,
                password=form_registro.password.data,
                tipo_usuario='public'
            )
            if agregar_usuario(nuevo_usuario):
                print('Se registro')
                session['email']=nuevo_usuario.email
                session['tipo_usuario']='public'
                flash(_("You have successfully registered!!!"),'success')
                msg = Message(_('Thanks for your register!'),
                          sender=MAIL_USERNAME,
                          recipients=[nuevo_usuario.email])
                # print(f"Mensaje... {msg}")

                msg.html = render_template('email.html', username=nuevo_usuario.nombres)
                mail.send(msg)
                return redirect(url_for('inicio.home'))
            else:
                print('Problema de registro')
                flash(_('There was a problem during registration. Please try again.'),'danger')
                return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())

    elif form_login.submit_login.data and form_login.validate_on_submit():
        # Llega el formulario de login
        correo_login=form_login.email.data
        existe_usuario=obtener_por_email(correo_login)
        if existe_usuario:
            print('Correo existe')
            if(existe_usuario.password==form_login.password_l.data):
                session['email']=existe_usuario.email
                session['tipo_usuario']=existe_usuario.tipo_usuario
                print('Inicio de sesion exitoso')
                flash(_('Successful login'),'success')
                print(f"***Tipo de usuario***{existe_usuario.tipo_usuario}")

                if existe_usuario.tipo_usuario=='admin':
                    # Si el usuario esta regisrrado como un administrador
                    return redirect(url_for('admin.panel_control'))
                else:
                    return redirect(url_for('inicio.home'))
            else:
                print('Contraseña incorrecta')
                flash(_('Password is incorrect. Try again.'),'warning')
            return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())
        else:
            # Si el correo no está registrado
        
            flash(_('The email entered is not registered. If you do not have an account you must register'),'warning')
            return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())

    else:
        

        return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())

@auth_bp.route('/cerrar_sesion')
def cerrar_sesion():
    """Cierra la sesión del usuario"""
    # Eliminar la clave 'email' de la sesión
    session.pop('email', None)
    session.pop('tipo_usuario', None)
    return redirect(url_for('inicio.home'))


#REESTABLECER CONTRASEÑA

def send_reset_email(user:Usuario):
    token = user.get_reset_token()
    msg = Message(_('Password Reset Request'),
                  sender=MAIL_USERNAME,
                  recipients=[user.email])
    msg.body = _(f'''To reset your password, visit the following link:
        {url_for('auth.reset_token', token=token, _external=True)}
        If you have not requested this, simply ignore this email and no action will be taken.
    ''')
    mail.send(msg)

@auth_bp.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if 'email' in session:
        if session['tipo_usuario']=='admin':
            return redirect(url_for('admin.panel_control'))
        return redirect(url_for('inicio.home'))
    
    cart = obtener_carrito()
    if request.method == 'POST':
        email = request.form.get('email')
        user = obtener_por_email(email=email)
        if user:
            send_reset_email(user)
            flash(_('An email has been sent with instructions to reset your password.'),'success')
            return redirect(url_for('auth.login_registro'))
        else:
            flash(_('There is no account with that email. Sign up first.'), 'warning')
    return render_template('reset_request.html',total_items_cart=cart.total_items())

@auth_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if 'email' in session:
        if session['tipo_usuario']=='admin':
            return redirect(url_for('admin.panel_control'))
        return redirect(url_for('inicio.home'))
    
    cart = obtener_carrito()
    user = Usuario.verify_reset_token(token)
    if user is None:
        flash(_('The token is invalid or has expired.'), 'warning')
        return redirect(url_for('auth.reset_request'))
    if request.method == 'POST':
        password = request.form.get('password')
        user.password = password
        user.reset_token = None
        if actualizarUsuario(user):    
            flash(_('Your password has been updated. Now you can log in.'),'success')
            return redirect(url_for('auth.login_registro'))
        else:
            flash(_('An error occurred while resetting'),'danger')
    return render_template('reset_token.html', token=token, total_items_cart=cart.total_items())
