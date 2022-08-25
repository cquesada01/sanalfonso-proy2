from flask import Flask, Blueprint, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL

app = Flask(__name__)

app.static_folder = 'static'

db = MySQL(app)

resultados1 = Blueprint('resultados1', __name__)

#Modelos
from models.ModelResultado1 import ModelResultado1

#Entidades
from models.entities.Resultado1 import Resultado1

@resultados1.route('/test_1', methods=['GET','POST'])
@login_required
def register():
    if request.method == 'POST':
           usuarios_id = current_user.id
           q1 = request.form['q1']
           q2 = request.form['q2']
           q3 = request.form['q3']
           q4 = request.form['q4']
           resultado = Resultado1(0,q1,q2,q3,q4,usuarios_id)
           ModelResultado1.register(db,resultado)
           flash("respuestas enviadas con éxito", category="success")
           return render_template('auth/test_1.html')
    return render_template('auth/test_1.html')







