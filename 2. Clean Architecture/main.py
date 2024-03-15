from flask import Flask, request, jsonify
from UseCase import UseCase
from DatabaseAdapter import DatabaseAdapter

app = Flask(__name__)

adaptador_db = DatabaseAdapter('baseusuarios.db')
adaptador_db.conectar()
caso_de_uso = UseCase()

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos_usuario = request.json
    nuevo_usuario = caso_de_uso.crear_usuario(datos_usuario['nombre'], datos_usuario['correo_electronico'], datos_usuario['contraseña'])
    adaptador_db.guardar_usuario(nuevo_usuario)
    return jsonify({'mensaje': 'Usuario creado correctamente'}), 200


if __name__ == '__main__':
    app.run(debug=True)