from base_datos import db
class LibroModel(db.Model):
      __tablename__="t_libro"
      id = db.Column("lib_id", db.Integer, primary_key=True)
      nombre = db.Column("lib_nomb", db.String(45))
      editorial = db.Column("lib_editarial", db.String(45))
      numpaginas = db.Column('lib_numpag', db.Integer)
      precio = db.Column("lib_precio", db.DECIMAL(5,2))
      publicacion = db.Column("lib_publicacion", db.String(4))
      codigo = db.Column("lib_cod", db.Text)
      estado = db.Column(db.Boolean, default=True)
#RELACIONES
      est_id = db.Column(db.Integer, db.ForeingnKey('t_estante.est_id') , nullable=False)
      autores = db.relationship('AutorLibroModel', backref='libro')

    def __init__(self, nombre, editorial, numpaginas, precio, publicacion, codigo, estante, estado ):
        self.nombre = nombre
        self.editorial = editorial
        self.numpaginas = numpaginas
        self.precio = precio
        self.publicacion = publicacion
        self.codigo = codigo
        self.est_id = estante
        self.estado = estado   
    
    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()

    def mostrar_json(self):
        return{
           'id': self.id,
           'nombre': self.nombre,
           'num_paginas': self.numpaginas,
           'precio': float(self.precio),
           'publicacion':self.publicacion,
           'codigo':self.codigo,
           'estante':self.est_id,
           'estado':self.estado 
        }    