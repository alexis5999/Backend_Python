from django.db import models

# Create your models here.
# Modelo llamado Clientes
class Clientes (models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
# aquí creamos la foto y lo sube a la carpeta de fotos
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre    


