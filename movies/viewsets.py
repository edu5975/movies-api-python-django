from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated

class ActorViewset(viewsets.ModelViewSet):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer

class DirectorViewset(viewsets.ModelViewSet):
    queryset = models.Director.objects.all()
    
    print(queryset)
    serializer_class = serializers.DirectorSerializer

class GeneroViewset(viewsets.ModelViewSet):
    queryset = models.Genero.objects.all()
    serializer_class = serializers.GeneroSerializer

class ClasificacionViewset(viewsets.ModelViewSet):
    queryset = models.Clasificacion.objects.all()
    serializer_class = serializers.ClasificacionSerializer

class PeliculasViewset(viewsets.ModelViewSet):
    queryset = models.Peliculas.objects.all()
    serializer_class = serializers.PeliculasSerializer

class RepartoViewset(viewsets.ModelViewSet):
    queryset = models.Reparto.objects.all()
    serializer_class = serializers.RepartoSerializer