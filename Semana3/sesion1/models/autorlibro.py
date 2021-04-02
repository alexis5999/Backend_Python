from base_datos import db
class AutorLibroModel(db.Model):
    __tablename__="t_autorlibro"
    id = db.Column("aut_lib_id",db.Integer, primary_key=True)
    lib_id = db.Column(db.Integer, db.ForeignKey('t_libro.lib_id'), nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('t_autor.autor_id'), nullable=False)
    estado = db.Column(db.Boolean, default=True)
    def __init__(self, libro, autor, estado):
        self.lib_id = libro
        self.autor_id = autor
        self.estado = estado