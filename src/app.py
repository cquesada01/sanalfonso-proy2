from flask import Flask, redirect, render_template, request, url_for , flash, abort, session
from flask_mail import Mail, Message
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from routes.perfiles import perfiles
from routes.usuarios import usuarios
from routes.resultados1 import resultados1
from werkzeug.security import generate_password_hash
import uuid
#rom flask_sqlalchemy import SQLAlchemy


from flask_wtf.csrf import CSRFProtect

from config import config

#Modelos
from models.ModelUser import ModelUser


#Entities
from models.entities.User import User


csrf = CSRFProtect()

app = Flask(__name__)

app.static_folder = 'static'

db = MySQL(app)

login_manager_app = LoginManager(app)

app.register_blueprint(perfiles)

app.register_blueprint(usuarios)

app.register_blueprint(resultados1)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #print(request.form['username'])
        #print(request.form['password'])
        user = User(0, request.form['username'],request.form['password'])
        logged_user=ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password and logged_user.tipo=='ADMIN':
                login_user(logged_user)
                return redirect(url_for('admin'))
            if logged_user.password and logged_user.tipo=='GUEST':
                login_user(logged_user)
                return redirect(url_for('student'))
            else:
                flash("credenciales incorrectas",category="error" )
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado en la base de datos", category="error")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

    
@app.route('/logout')
def logout():
    logout_user()
    flash("Sesión finalizada", category="info")
    return redirect(url_for('login'))   

@app.route('/home')
@login_required
def home():
    flash("Inicio de sesión correcto", category="success")
    return render_template('auth/home.html')

@app.route('/admin')
@login_required
def admin():
    flash("Inicio de sesión correcto", category="success")
    return render_template('auth/admin.html')

@app.route('/student')
@login_required
def student():
    flash("Inicio de sesión correcto", category="success")
    return render_template('auth/perfil.html')

@app.route('/forgot', methods=['GET','POST'])
def forgot():
    if 'login' in session:
        return redirect('/')
    if request.method == "POST":
        username = request.form['username']
        token = str(uuid.uuid4())
        cur = db.connection.cursor()
        result = cur.execute("SELECT * FROM usuarios WHERE username=%s" , [username])
        if result > 0:
            data = cur.fetchone()
            msg = Message(subject="Solicitud de reinicio de contraseña", sender="cesar_quesada1@usmp.pe", recipients=[username])
            msg.html = render_template('auth/sent.html', token=token, data=data)
            mail = Mail(app)
            mail.send(msg)
            cur = db.connection.cursor()
            cur.execute("UPDATE usuarios SET token=%s WHERE username=%s" , [token,username])
            db.connection.commit()
            cur.close()
            flash("Un email fue enviado a su correo, revise su bandeja", category="success")
            return redirect('/forgot')
        else:
            flash("El email ingresado no fue encontrado", category="warning")
            return redirect('/forgot')
    return render_template("auth/forgot.html")


@app.route('/reset/<token>' , methods=["POST","GET"])
def reset(token):
    if 'login' in session:
        return redirect(url_for('login')) 
    if request.method == "POST":
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        token1 = str(uuid.uuid4())
        if password != confirm_password:
            flash("Las contraseñas no coinciden", category="warning")
            return render_template('auth/reset.html')
        password = generate_password_hash(password)
        cur = db.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE token=%s" , [token])
        user = cur.fetchone()
        if user:
            cur = db.connection.cursor()
            cur.execute("UPDATE usuarios SET token=%s, password=%s WHERE token=%s" , [token1, password, token])
            db.connection.commit()
            cur.close()
            flash("Se ha actualizado la contraseña", category="success")
            return redirect('/login')
        else:
            flash("Su token es invalido o ha expirado", category="warning")
            return redirect('/')      
    return render_template('auth/reset.html')



def status_401(error):
    return redirect(url_for('login'))

""" def status_404(error):
    return "<h1>'Página no encontrada'</h1>" """



if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    #app.register_error_handler(404,status_404)
    app.run()



