from django.db import models

# Create your models here.
class Actor(models.Model):
    nombre = models.TextField()
    nacionalidad = models.TextField()

class Director(models.Model):
    nombre = models.TextField()
    nacionalidad = models.TextField()

class Genero(models.Model):
    descripcion = models.TextField()

class Clasificacion(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField()

class Peliculas(models.Model):
    titulo = models.TextField()
    duracion = models.IntegerField()
    sinopsis = models.TextField()
    fechaestreno = models.DateTimeField()
    clasificacion = models.ForeignKey("Clasificacion",on_delete=models.CASCADE)
    genero = models.ForeignKey("Genero",on_delete=models.CASCADE)
    director = models.ForeignKey("Director",on_delete=models.CASCADE)

class Reparto(models.Model):
    personaje = models.TextField()
    actor = models.ForeignKey("Actor",related_name="reparto_actor",on_delete=models.CASCADE)    
    pelicula = models.ForeignKey("Peliculas",on_delete=models.CASCADE)