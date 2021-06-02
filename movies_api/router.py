from movies.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('actor',ActorViewset)
router.register('director',DirectorViewset)
router.register('genero',GeneroViewset)
router.register('clasificacion',ClasificacionViewset)
router.register('peliculas',PeliculasViewset)
router.register('reparto',RepartoViewset)

# GET, POST, PUT, DELETE
# list , retrive
