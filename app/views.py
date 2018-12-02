from app import app
from flask import render_template, flash, redirect, session, url_for, request, jsonify
from datetime import datetime , time , date
import psycopg2

conn = psycopg2.connect("dbname=pyproyecto host=localhost user=tics1 password=12345")
cur = conn.cursor()


@app.route('/', methods = ['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def home_login():
    if request.method is 'POST':
        rut = request.form['rut']
        contrasena = request.form['psw']

        sql="""SELECT rut,contrasena FROM usuario WHERE usuario.rut = '%s' AND usuario.contrasena = '%s';
		"""%(rut, contrasena)
        cur.execute(sql)
        resultados = cur.fetchall()

        sql="""SELECT nombre,apellido FROM usuario WHERE usuario.rut = '%s';
		"""%(rut)
        cur.execute(sql)
        Nombrecompleto = cur.fetchall()

        if resultados is None:
            alerta="cuenta invalida"
            return render_template("login.html", alerta = alerta)

        elif resultados[1] is not contrasena:
            alerta="contrasena invalida"
            return render_template("login.html", alerta = alerta)
        else:
            return redirect(url_for("sesion_init"))
    else:
        return render_template("login.html")


@app.route('/sesiones', methods=['GET','POST'])
def sesion_init():
    if request.method is 'POST':
        return render_template("index.html")
    return render_template("index.html")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method is 'POST':
        password=request.form["psw"]
        rut=request.form["rut"]
        nombre=request.form["nombre"]
        apellido=request.form["apellido"]

        sql="""SELECT * FROM usuario WHERE usuario.rut ='%s';"""%(rut)
        cur.execute(sql)
        resultado = cur.fetchall()

        if len(rut) >10 and len(rut) < 9:
            alerta="Rut invalido"
            return render_template("registrar.html", alerta = alerta)

        elif len(resultado) is 0 :
            sql ="""INSERT INTO usuario (rut, apellido, nombre, contrasena) VALUES ('%s','%s','%s','%s');"""%(rut, apellido, nombre, password)
            cur.execute(sql)
            aviso="Usuario creado!!"
            return render_template("registrar.html", aviso = aviso, password= password, rut= rut, nombre= nombre, apellido=apellido)

        elif len(resultado) != 0:
            alerta="Rut ya utilizado"
            return render_template("registrar.html", alerta = alerta)
        else:
            return render_template("registrar.html",alerta=alerta)

    else:
        return render_template("registrar.html")

@app.route('/about', methods = ['GET'])
def about():
    return render_template('acerca.html')
