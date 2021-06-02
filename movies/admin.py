from django.contrib import admin
from .models import Actor, Director, Genero, Clasificacion, Peliculas, Reparto

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genero)
admin.site.register(Clasificacion)
admin.site.register(Peliculas)
admin.site.register(Reparto)

