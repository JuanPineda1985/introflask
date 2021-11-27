from bson import objectid
from flask import Flask, request, Response, jsonify
from werkzeug.wrappers import response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

#conexion a Servidor Mongo
app.config['MONGO_URI'] = 'mongodb://localhost:27017/dbBibliotek'
mongo = PyMongo(app)

#EndPoints

@app.route('/Libros', methods=['POST'])
def add_libro():
    nombre = request.json['nombre']
    precio = request.json['precio']
    if nombre and precio:
        id = mongo.db.books.insert(
            {'nombre':nombre, 'precio':precio}
        )
        response=jsonify({'mensaje':'libro agregado correctamente'})
        return response

@app.route('/Libros', methods=['GET'])
def get_libros():
    libros = mongo.db.libros.find()
    response = json_util.dumps(libros)
    return Response(response, mimetype="application/json")

@app.route('/Libros/<id>', methods={'GET'})
def get_libro(id):
    libro = mongo.db.libros.find_one({'_id': objectid(id)})
    response = json_util.dumps(libro)
    return Response(response, mimetype="application/json")

@app.route('/Libros/<id>', methods=['DELETE'])
def delete_libro(id):
    mongo.db.libros.delete_one({'_id':objectid(id)})
    response = jsonify({'message': 'libro' + id + 'ha sido borrado'})
    return response

@app.route('/books/<id>', methods=['PUT'])
def update_libro(_id):
    nombre = request.json['nombre']
    precio = request.json['precio']
    if nombre and precio and _id:
        mongo.db.libro.update_one(
            {'_id': objectid(_id['$oid']) if '$oid' in _id else objectid(_id)}, {'$set': {'nombre': nombre, 'precio': precio}})
        response = jsonify({'message': 'libro' + _id + 'ha sido actualizado' })
        return response

if __name__ == "__main__":
    app.run(debug=True, port=5600)