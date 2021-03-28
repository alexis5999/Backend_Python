 #pip install flask
from flask import Flask, request
# pip install flask-cors
# pip install flask-cors --upgrade
from flask_cors import CORS
# Crear una instancia de la clase
app = Flask(__name__)
# HABILITAR LOS ACCESOS (CORS) PARA TODOS LOS DOMINIOS Y TODOS LOS VERBOS HTTP
CORS(app)
tiendas = []
# Es un ENDPOINT
# 127.0.0.1:9000/
# localhost:9000/
@app.route("/")
def inicio():
    return "Servidor Corriendo FLASK"
# Los verbos HTTP mas comunes para poder trabajar son :
#GET => Se usa para solicitar  información sin manda o enviar nada por el body
#POST => Se una para crear y mandar información
#PUT => Se usa para poder actualizar algún registro o información
#DELETE => Se usa para poder realizar la eliminación de algún regitro 

@app.route("/tienda/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def  tienda(id):
    if len(tiendas) > id:
        if request.method == "GET":
            return {
              "ok": True,
              "content": tiendas[id],
              "message": None
            }
        elif request.method == "PUT":
            data = request.get_json()
            tiendas[id] = data
            return {
              "ok": True,
              "content": tiendas[id],
              "message": "Se actualizo la tienda comercial correctamente"
            }, 201
        elif request.method == "DELETE":
             # Existen 3 metodos pop(id)- remove("se manda lo que contiene")
             # 1 forma
            tienda = tiendas.pop(id)
            return {
             "ok": True,
              "content": tienda,
              "message": "Se elimino la tienda comercial correctamente"
            }, 200
            # 2 forma
            del tiendas[id]
            return {
             "ok": True,
              "content": None,
              "message": "Se elimino la tienda comercial correctamente"
            }, 200
        else:
            return {
             "ok": False,
              "content": None,
              "message": "La tienda no Existe"
            }

@app.route("/tienda/buscar/<string:palabra>")
def buscador(palabra):
    resultado = []
    for tienda in tiendas:
        print(palabra.lower())
        if palabra.lower() in tienda['nombre'].lower():
            resultado.append(tienda)
    if resultado:
             return {
             "ok": True,
              "content": resultado,
              "message": None
            }
    else:
             return {
             "ok": False,
              "content": "No hay resultados",
              "message": None
            }, 404

@app.route("/tiendas", methods=["GET" , "POST"])    
def manejo_tiendas():
    print(request.method)
    if request.method == "GET":
        if tiendas:
            return {
             "ok": True,
              "content": tiendas,
              "message": None
            }
        else:
            return {
             "ok": False,
              "content": None,
              "message": "No hay tiendas"
            }, 404
    elif  request.method == "POST":
        # El metodo get_json Automaticamente transforma el Json enviado por el front a un
        # dicccionario
       data = request.get_json()
       tiendas.append(data)
       return {
             "ok": True,
              "content": None,
              "message": "La tienda se agrego exitosamente"
            }, 201   

app.run(debug=True, port=9000)