from flask import Flask, Blueprint, request, flash, render_template, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_mysqldb import MySQL

app = Flask(__name__)

app.static_folder = 'static'

db = MySQL(app)

perfiles = Blueprint('perfiles', __name__)

#Modelos
from models.ModelPerfil import ModelPerfil

#Entidades
from models.entities.Perfil import Perfil

@perfiles.route('/register', methods=['GET','POST'])
@login_required
def register():
    if request.method == 'POST':
           curso = request.form['curso']
           carrera = request.form['carrera']
           habilidad = request.form['habilidad']
           universidad = request.form['universidad']
           perfil = Perfil(0,curso,carrera,habilidad,universidad)
           ModelPerfil.register(db,perfil)
           flash("perfil añadido", category="success")
           return render_template('auth/perfil.html')
    return render_template('auth/perfil.html')


@perfiles.route('/read')
@login_required
def read():
    data_perfil = ModelPerfil.read(db)
    flash("se recuperaron la lista de perfiles", category="info")
    return render_template('auth/listado.html', perfiles=data_perfil)
    

@perfiles.route('/delete/<string:id>', methods=["GET"])
@login_required
def delete(id):
    ModelPerfil.delete(db,id)
    flash("se elimino la entrada seleccionada", category="warning")
    return redirect(url_for('perfiles.read'))


@perfiles.route('/update', methods=["POST"])
@login_required
def update():
    if request.method == 'POST':
        id = request.form['id']
        curso = request.form['curso']
        carrera = request.form['carrera']
        habilidad = request.form['habilidad']
        universidad = request.form['universidad']
        ModelPerfil.update(db,curso,carrera,habilidad,universidad,id)
        flash("se actualizaron los datos", category="success")
        return redirect(url_for('perfiles.read'))
    return redirect(url_for('perfiles.read'))