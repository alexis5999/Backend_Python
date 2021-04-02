from base_datos import db
class AutorModel(db.Model):
    __tablename__="t_autor"
    id = db.Column("autor_id",db.Integer, primary_key=True)
    nombre = db.Column("autor_nomb", db.String(45), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    libros = db.relationship('AutorLibroModel', backref='autor')

    def __init__(self, nombre, estado):
        self.nombre = nombre
        self.estado = estado