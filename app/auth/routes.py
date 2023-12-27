from flask import current_app, render_template, request, redirect, url_for, session, flash
from app.auth.forms import LoginForm, RegistroForm
from app.config.config import Config, MAIL_USERNAME, mail
from app.models.usuario import Usuario
from app.services.cart import obtener_carrito
from app.services.auth_service import verificar_email, verificar_password
from app.services.usuario_service import agregar_usuario, obtener_por_email
from . import auth_bp
from flask_mail import Mail, Message



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
            flash('El correo electrónico ya está registrado. Inicia sesión si ya tienes una cuenta.')
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
                flash("Te has registrado exitosamente!!!")
                msg = Message('Gracias por tu registro!',
                          sender=MAIL_USERNAME,
                          recipients=[nuevo_usuario.email])
                # print(f"Mensaje... {msg}")

                msg.html = render_template('email.html', username=nuevo_usuario.nombres)
                mail.send(msg)
                return redirect(url_for('inicio.home'))
            else:
                print('Problema de registro')
                flash('Hubo un problema durante el registro. Por favor, inténtalo de nuevo.')
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
                flash('Inicio de sesion exitoso','success')
                print(f"***Tipo de usuario***{existe_usuario.tipo_usuario}")

                if existe_usuario.tipo_usuario=='admin':
                    # Si el usuario esta regisrrado como un administrador
                    return redirect(url_for('admin.panel_control'))
                else:
                    return redirect(url_for('inicio.home'))
            else:
                print('Contraseña incorrecta')
                flash('La contraseña es incorrecta. Intenta nuevamente.')
            return render_template("login.html", form_registro=form_registro, form_login=form_login, total_items_cart=cart.total_items())
        else:
            # Si el correo no está registrado
        
            flash('Hubo un problema, el correo ingresado no está registrado')
            flash('Si no tienes cuenta debes registrarte')
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

