from flask import Flask
# pip install flask-restful
from flask_restful import Api
# pip install flask-sqlalchemy
from base_datos import db
# from models.estante import EstanteModel
from controllers.estante import EstantesController, EstanteController
from models.autor import AutorModel
# from models.libro import LibroModel
from controllers.libro import LibrosController, LibroController, EncontrarLibroController
from models.autorlibro import AutorLibroModel

app = Flask(__name__)
# dialect+driver://username:password@host:port/database
# es compatible con MySQL, Oracle, PostgreSQL, SQLite
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost/libreria'
api = Api(app=app)
@app.before_first_request
def iniciador():
    # Aca se conecta al servidor
    db.init_app(app)
    # Eliminacion de los modelos, x defecto elimina todos
    # db.drop_all(app=app)
    # Creacion de los Modelos
    db.create_all(app=app)

@app.route("/")
def inicio():
    return 'El servidor funciona correctamente'

# DEFINIR MIS RUTAS
api.add_resource(EstantesController,'/estante')
api.add_resource(EstanteController, '/estante/<int:est_id>')
api.add_resource(LibrosController, '/libro')
api.add_resource(LibroController, '/libro/<int:lib_id>')
api.add_resource(EncontrarLibroController,'/libro/<string:palabra>')

if __name__ == '__main__':
    app.run(debug=True)