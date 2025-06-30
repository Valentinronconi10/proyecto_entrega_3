from django.urls import path
from .views import inicio, artistas, albumes, canciones, albumFormulario2, artistaFormulario, cancionFormulario, busquedaCancion, buscar


urlpatterns = [
    path('', inicio, name='inicio'),                        # views.inicio
    path('artistas/', artistas, name='artistas'),           # views.artistas
    path('albumes/', albumes, name='albumes'),              # views.albumes
    path('canciones/', canciones, name='canciones'),        # views.canciones
    path('album_formulario/', albumFormulario2, name='albumFormulario2'),   # views.albumFormulario2
    path('artista_formulario/', artistaFormulario, name='artistaFormulario'), # views.artistaFormulario
    path('cancion_formulario/', cancionFormulario, name='cancionFormulario'), # views.cancionFormulario
    path('busquedaCancion/', busquedaCancion, name='busquedaCancion'),      # views.busquedaCancion
    path('buscar/', buscar, name='buscar'),                 # views.buscar
]