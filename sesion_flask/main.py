from flask import Flask, request, render_template, redirect, url_for, flash, session #Session va a quedar con una serie de posiciones

app= Flask(__name__)
app.secret_key ='wagh'

@app.route('/')
def index():
    return render_template('/login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        #capturar datos enviados
        email= request.form['email']
        password = request.form['password']
        rol = request.form['rol']
        #Creacion de variables de SESION
        session['email']=email
        session['password']=password
        session['rol']=rol
        return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    if session['email']=='xx@gmail.com' and session['password']=='11' and session['rol']=='admin':
        return render_template('cart.html')
    else:
        #return "No tiene permiso para ingresar a este usuario"
        return redirect('/')

@app.route('/logout')
def logout():
    #Borrar el contenido de las variables de session
    session.clear() #destruye las variables de sesion
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=2300)