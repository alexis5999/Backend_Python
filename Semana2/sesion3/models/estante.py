from base_datos import db
class EstanteModel(db.Model):
    __tablename__="t_estante"
    id = db.Column("est_id",db.Integer, primary_key=True)
    capacidad = db.Column("est_cap", db.Integer, nullable=False)
    ubicacion = db.Column("est_ubic", db.String(50))
    descripcion = db.Column("est_desc", db.String(45))
    estado = db.Column(db.Boolean, default=True)
    # Voy a crear mi relacion inversa
    # sirve para hacer la relacion inversa (traer todos los libros que pertenecen
    # a un estante) y nos ayuda demasiado para la logica
    libros = db.relationship('LibroModel', backref='estante')

    def __init__(self, capacidad, ubicacion, descripcion, estado=None):
        self.capacidad = capacidad
        self.ubicacion = ubicacion
        self.descripcion = descripcion
        if estado is not None:
            self.estado = estado
    
    def guardar_bd(self):
        db.session.add(self)
        db.session.commit()
    
    def mostrar_json(self):
        return {
            'id':self.id,
            'capacidad':self.capacidad,
            'ubicacion':self.ubicacion,
            'descripcion': self.descripcion,
            'estado': self.estado
        }
    def __str__(self):
        return '%s, %s, %s'%(self.id, self.capacidad, self.ubicacion)