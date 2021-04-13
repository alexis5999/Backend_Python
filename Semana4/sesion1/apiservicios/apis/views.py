from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Clientes
from .serializers import *

class ClientesList (viewsets.ModelViewSet):
     queryset = Clientes.objects.all()
     serializer_class = ClienteSerializer


# Create your views here.
