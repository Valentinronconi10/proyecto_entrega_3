from django.urls import path
from AppProyecto.views import *
from django.contrib.auth.views import LogoutView

from AppProyecto.eliminar.eliminar_album import AlbumDeleteView
from AppProyecto.eliminar.eliminar_artista import ArtistaDeleteView
from AppProyecto.eliminar.eliminar_cancion import CancionDeleteView
from AppProyecto.editar_views.editar_album import AlbumUpdateView
from AppProyecto.editar_views.editar_cancion import CancionUpdateView
from AppProyecto.editar_views.editar_artista import ArtistaUpdateView
from AppProyecto.detalle_views.album_detail import AlbumDetailView
from AppProyecto.detalle_views.cancion_detail import CancionDetailView  
from AppProyecto.detalle_views.artista_detail import ArtistaDetailView

urlpatterns = [
    path('', inicio, name='inicio'),                        # views.inicio
    path('artistas/', artistas, name='artistas'),           # views.artistas
    path('albumes/', albumes, name='albumes'),              # views.albumes
    
    path('canciones/', canciones, name='canciones'),        # views.canciones
    path('about_me/', about_me, name='about_me'),
    path('contacto/', contacto, name='contacto'),

    path('login/', login_request, name='login_request'),
    path('registro/', register, name= 'registro'),
    path('logout/', LogoutView.as_view(template_name="AppProyecto/usuario/logout.html"), name= 'logout'),

    #path('album_formulario/', albumFormulario2, name='albumFormulario2'),   # views.albumFormulario2
    #path('artista_formulario/', artistaFormulario, name='artistaFormulario'), # views.artistaFormulario
    #path('cancion_formulario/', cancionFormulario, name='cancionFormulario'), # views.cancionFormulario
    path('busquedaCancion/', busquedaCancion, name='busquedaCancion'),      # views.busquedaCancion
    path('buscar/', buscar, name='buscar'),                 # views.buscar


    #path('album/create', album_create, name='album_create'),
    path('album/create/', AlbumCreateView.as_view(), name= 'album_create'),
    path('artista/create/', ArtistaCreateView.as_view(), name='artista_create'),
    path('cancion/create/', CancionCreateView.as_view(), name='cancion_create'),
    
    
    path('leerAlbumes/', leer_albumes, name='leerAlbumes'),  # views.leer_albumes
    path('leerCanciones/', leer_canciones, name='leerCanciones'),  # views.leer_albumes
    path('leerArtistas/', leer_artistas, name='leerArtistas'),  # views.leer_albumes
    
    

    path('album_eliminar/<int:pk>/', AlbumDeleteView.as_view(), name='eliminar_album'),  # eliminar.eliminar_album.AlbumDeleteView
    path('eliminar_artista/<int:pk>/', ArtistaDeleteView.as_view(), name='eliminar_artista'),  # eliminar.eliminar_artista.ArtistaDeleteView
    path('eliminar_cancion/<int:pk>/', CancionDeleteView.as_view(), name='eliminar_cancion'),

    
    path('editarAlbum/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('editarCancion/<int:pk>/', CancionUpdateView.as_view(), name='cancion_update'),
    path('editarArtista/<int:pk>/', ArtistaUpdateView.as_view(), name='artista_update'),

    path('albumDetail/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('artistaDetail/<int:pk>/', ArtistaDetailView.as_view(), name='artista_detail'),
    path('cancionDetail/<int:pk>/', CancionDetailView.as_view(), name='cancion_detail'),
]


