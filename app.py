from flask import Flask, render_template, redirect, url_for
from flask.json import jsonify
from flask_mysqldb import MySQL
from flask import jsonify


app = Flask(_name_)
# enpoint o rutas

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdflask'

conexion = MySQL(app) 

@app.route('/car')
def listar_car():
    data ={}
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, marca, modelo, valor FROM car ORDER BY marca"
        cursor.execute(sql)
        car = cursor.fetchall()
        data['car'] = car
    except Exception as ex:
        data['mensaje'] = 'Error...'
    return jsonify(data)


@app.route('/')
def index():
    #return "<h1>Hola, desde la pagina de incio</h1>"
    vehiculos = ['Mazda', 'Chevrolet', 'Renault', 'Audi']
    datosindex = {
        'titulo': 'Sistema de pruebas', 
        'subtitulo': 'Bienvenido al sitema usuario: ',
        'vehiculos':vehiculos, 
        'usuario': 'usuarioprueba',
        'referencias': ['2', 'Aveo', 'Logan', '5 power', 'Airton'],
        'cantvehiculos': len(vehiculos)
    }
    return render_template('index.html', data= datosindex)

@app.route('/login')
def login():
    return render_template('login.html')

def not_found(error):
    #return render_template("not_found.html"), 404
    return redirect(url_for('index'))
app.register_error_handler(404, not_found)

if _name_ == "_main_":
    app.run(debug=True, port=3200)