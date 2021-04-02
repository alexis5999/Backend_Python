from flask_restful import Resource, reqparse
from models.libro import LibroModel

class LibrosController(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        "nombre",
        type=str,
        required=True,
        help="Falta ingresar el Nombre del Libro"
    )
    parser.add_argument(
        "editorial",
        type=str,
        required=True,
        help="Falta ingresar la Editorial del Libro"
    )
    parser.add_argument(
        "numpaginas",
        type=int,
        required=True,
        help="Falta ingresar el numero de página del Libro"
    )
    parser.add_argument(
        "precio",
        type=float,
        required=True,
        help="Falta ingresar el precio del Libro"
    )
    parser.add_argument(
        "publicacion",
        type=str,
        required=True,
        help="Falta ingresar la publicacion del Libro"
    )
    parser.add_argument(
        "codigo",
        type=str,
        required=True,
        help="Falta ingresar el Codigo del Libro"
    )
    parser.add_argument(
        "estante",
        type=str,
        required=True,
        help="Falta ingresar la ubicacion del Libro en el Estante"
    )
    parser.add_argument(
        "estado",
        type=bool,
        required=True,
        help='Falta ingresar el estado del Libro'
    )
    def get(self):
        libros = LibroModel.query.all()
        resultado = []
        for libro in libros:
            # print(libro)
            temporal = libro.mostrar_json()
            temporal['estante'] = libro.estante.mostrar_json()
            resultado.append(temporal)
            print(libro.estante.mostrar_json())
            # print(libro.est_id)
        return {
            'ok':True,
            'content':resultado
        }
    def post(self):
        data = self.parser.parse_args()
        libro = LibroModel(data['nombre'],data['editorial'],data['numpaginas'], data['precio'], data['publicacion'], data['codigo'],data['estante'],data['estado'])
        try:
            libro.guardar_bd()
            print(libro)
            return {
                'ok':True,
                'message':'Se guardo exitosamente el Libro',
                'content': libro.mostrar_json()
            }
        except:
            return {
                'ok':False,
                'message':'No se pudo guardar el Libro en la bd'
            },500

class LibroController(Resource):
    def get(self, lib_id):
        libro = LibroModel.query.filter_by(id=lib_id).first()
        informacion = libro.mostrar_json()
        estantef = libro.estante.mostrar_json()
        informacion['estante'] = estantef
        if libro:
            return {
                'ok':True,
                'content':informacion,
                'message':None
            }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el libro con id: '+str(lib_id)
            }, 404

    def put(self, lib_id):
        libro = LibroModel.query.filter_by(id=lib_id).first()
        if libro:
            parser = reqparse.RequestParser()
            parser.add_argument(
                "nombre",
                type=str,
                required=True,
                help="Falta el nombre del libro"
            )
            parser.add_argument(
                "editorial",
                type=str,
                required=True,
                help="Falta la editorial del libro"
            )
            parser.add_argument(
                "numpaginas",
                type=int,
                required=True,
                help="Falta el numero de paginas del libro"
            )
            parser.add_argument(
                "precio",
                type=float,
                required=True,
                help="Falta el precio"
            )
            parser.add_argument(
                "publicacion",
                type=int,
                required=True,
                help="Falta la año de publicacion"
            )
            parser.add_argument(
                "codigo",
                type=str,
                required=True,
                help="Falta el codigo"
            )
            parser.add_argument(
                "estado",
                type=bool,
                required=True,
                help="Falta el estado"
            )
            parser.add_argument(
                "est_id",
                type=int,
                required=True,
                help="Falta el estante"
            )

            data = parser.parse_args()
            libro.nombre = data['nombre']
            libro.editorial = data['editorial']
            libro.numpaginas = data['numpaginas']
            libro.precio = data['precio']
            libro.publicacion = data['publicacion']
            libro.codigo = data['codigo']
            libro.estado = data['estado']
            libro.est_id = data['est_id']

            libro.guardar_bd()

            return {
                'ok':True,
                'content':libro.mostrar_json(),
                'message':None
            }

        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el libro con el id: '+str(lib_id)
            }

    def delete(self, lib_id):
        libro = LibroModel.query.filter_by(id=lib_id).first()
        if libro:
            if libro.estado == True:
                libro.estado = False
                libro.guardar_bd()
                return {
                    'ok':True,
                    'content':None,
                    'message':'El libro fue deshabilitado correctamente'
                }
            else:
                return {
                    'ok':False,
                    'content':None,
                    'message':'El libro ya se encuentra deshabilitado'
                }
        else:
            return {
                'ok':False,
                'content':None,
                'message':'No existe el libro'
            }, 400

class EncontrarLibroController(Resource):
    def get(self, palabra):
        resultado = LibroModel.query.filter(LibroModel.nombre.like('%'+palabra+'%')).all()
        if resultado:
            respuesta = []
            for libro in resultado:
                respuesta.append(libro.mostrar_json())
            return{
                'Ok':True,
                'content':respuesta,
                'message':''
            }
        else:
            return{
                'Ok':False,
                'content':None,
                'message':'No se encontro ninguna coincidencia'
            }, 404