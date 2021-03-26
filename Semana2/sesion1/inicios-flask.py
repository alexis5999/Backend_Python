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
    return "Servidor Corriendo FLASK 111111111111111111111111111111"

app.run(debug=True, port=9000)