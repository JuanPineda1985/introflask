from flask import Flask, render_template, url_for, request, redirect
import flask
import userController

app = Flask(__name__)

@app.route('/')
@app.route("/index")
def index():
    users = userController.get_users()
    return render_template('index.html', user = users)

@app.route("/form_add_user")
def form_add_user():
    return render_template('add_user.html')
    
@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = userController.get_user_id(id)
    return render_template ('edit_user.html', user=user)

@app.route("/update.user")
def update_user():
    # obtener los datos del formulario que invocó este endpoint
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    userController.update_user(name, email, phone, password, id)
    return redirect('/')

if __name__ == "__main__":
    app.run(port = 3200, debug = True)