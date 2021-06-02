from rest_framework import serializers
from .models import Actor, Director, Genero, Clasificacion, Peliculas, Reparto

class ActorSerializer(serializers.ModelSerializer):
    reparto_actor = RepartoSerializer(many=true)
    class Meta:
        model = Actor
        fields = '__all__'

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'

class PeliculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peliculas
        fields = '__all__'

class RepartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparto
        fields = '__all__'
