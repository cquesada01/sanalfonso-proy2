from flask import Flask, Blueprint, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL

app = Flask(__name__)

app.static_folder = 'static'

db = MySQL(app)

usuarios = Blueprint('usuarios', __name__)

#Modelos
from models.ModelUser import ModelUser

#Entidades
from models.entities.User import User

@usuarios.route('/register_user', methods=['GET','POST'])
def register_user():
    if request.method == 'POST':
           username = request.form['username']
           password = request.form['password']
           fullname = request.form['fullname']
           tipo = request.form['tipo']
           usuario = User(0,username,password,fullname,tipo)
           ModelUser.register_user(db,usuario)
           flash("usuario registrado", category="success")
           return render_template('auth/adduser.html')
    return render_template('auth/adduser.html')


