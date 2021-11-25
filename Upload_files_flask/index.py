# paquete para el manejo de sistema Operativo
import os
from flask import Flask, app, render_template, redirect, request, flash
from werkzeug.utils import secure_filename #nos sirve para guardar informacion en el Sistema Operativo

#Estructura basica de Flask
app = Flask (__name__)
app.secret_key =  'pandajuan' #Sirve para encriptar cosas
#Vamos a configurar la carpeta para almacenas nuestras imagenes
app.config['UPLOAD_FOLDER'] = 'static/img'

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():
   if request.method == 'POST':
       f = request.files['ufile'] #este toma la infomacion y esta variable puede c
       filename = secure_filename(f.filename)
       f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
       flash("la imagen se ha subido correctamente...")
       return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=4500)