from rest_framework import serializers, viewsets
from .models import Clientes
# vamos serializar nuestro modelo
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Clientes
        fields =("id","nombre","apellidos","descripcion","foto")
         
