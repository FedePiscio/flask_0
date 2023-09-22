# Del paquete flask estamos importanto una sola CLASE: Flask
# jsonify nos permitira tranformar un objeto de python en un objeto json.
from flask import Flask, jsonify, request
from markupsafe import escape

# Creamos una Instancia de la clase
app = Flask(__name__) 

# La barra hace referencia a una cadena vacia.
@app.route('/')
# Lo que se hace luego es definir una duncion dependiendo la ruta que elija el usuario:
# Creamos una funcion sin parametros llamada index que retorna una cadena:
def index():
    return 'Index'

# Creamos otra ruta de trabajo: Ping Pong
@app.route('/ping')
def ping():
    return jsonify({"Mensaje": "pong"})

# Creamos otra ruta usuario pasandole una variable: string
@app.route('/usuarios/<string:nombre>')
def usuario_by_name(nombre):
    return jsonify({"name": nombre})

# Creamos otra ruta usuario pasandole una variable: int
@app.route('/usuarios/<int:id>')
def usuario_by_id(id):
    return jsonify({"id": id})

# NO HACER: por que esta estructura permite una inyeccion de codigo
@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

# Creamos una ruta GET recursos:
@app.route('/recursos', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "Lista de los intems de este recurso"})

# Creamos una ruta POST recursos:
@app.route('/recursos', methods = ['POST'])
def post_recursos():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]      # se maneja como un diccionario
    modelo = body["modelo"]  # se maneja como un diccionario

    # creamos una estructura mas compleja: el recurso que se crea: tiene esta estructura:
    return jsonify({"recurso": {
        "name": name,
        "modelo": modelo
    }})

# GET de un recurso en particular a traves de su ID: Ej: buscar en base de datos un registro:
@app.route('/recursos/<int:id>', methods = ['GET'])
def get_recursos_by_id(id):
    return jsonify({"recurso": {
        "name": "nombre correspondiente al  id",
        "modelo": "modelo correspondiente al id"
    }})

# primer linea nos permite controlar que el archivo funcione correctamente si se lanza de esta manera: python app.py
# es decir que python app.py se ejecute como un archivo principal.
if __name__ == '__main__':
    # Corremos la app: pasamos por parametro
    # debug = True indica que vamos a hacer las pruebas en modo de desarrollo.
    # port = indicamos en que puerto queremos ejecutarlo. 5000 es el puerto mas comun utilizado en aplicaciones de este tipo.
    app.run(debug=True, port=5000)



