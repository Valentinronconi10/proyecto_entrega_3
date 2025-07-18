from django.urls import path
from AppProyecto.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from AppProyecto.eliminar.eliminar_todo import *
from AppProyecto.editar_views.editar_todo import *
from AppProyecto.detalle_views.detalle_todo import *
from AppProyecto.views_al.todo import *

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
    path('editarPerfil/', editar_perfil, name= 'editarPerfil'),
    path('perfil/', perfil, name= 'perfil'),

    #path('album_formulario/', albumFormulario2, name='albumFormulario2'),   # views.albumFormulario2
    #path('artista_formulario/', artistaFormulario, name='artistaFormulario'), # views.artistaFormulario
    #path('cancion_formulario/', cancionFormulario, name='cancionFormulario'), # views.cancionFormulario
    path('busquedaCancion/', busquedaCancion, name='busquedaCancion'),      # views.busquedaCancion
    path('buscar/', buscar, name='buscar'),                 # views.buscar


    #path('album/create', album_create, name='album_create'),
    path('album/create/', AlbumCreateView.as_view(), name= 'album_create'),
    path('albumPop/create', AlbumCreateViewPop.as_view(), name= 'albumPop_create'),
    path('albumReggaeton/create', AlbumCreateViewReggaeton.as_view(), name= 'albumReggaeton_create'),



    path('artista/create/', ArtistaCreateView.as_view(), name='artista_create'),
    path('artistaPop/create/', ArtistaCreateViewPop.as_view(), name='artistaPop_create'),
    path('artistaReggaeton/create/', ArtistaCreateViewReggaeton.as_view(), name='artistaReggaeton_create'),

    path('cancion/create/', CancionCreateView.as_view(), name='cancion_create'),
    path('cancionPop/create/', CancionCreateViewPop.as_view(), name='cancionPop_create'),
    path('cancionReggaeton/create/', CancionCreateViewReggaeton.as_view(), name='cancionReggaeton_create'),
    
    
    path('leerAlbumes/', leer_albumes, name='leerAlbumes'),  # views.leer_albumes
    path('leerAlbumesPop/', leer_albumesPop, name='leerAlbumesPop'),  # views.leer_albumes
    path('leerAlbumesReggaeton/', leer_albumesReggaeton, name='leerAlbumesReggaeton'),  # views.leer_albumes
    path('leerCanciones/', leer_canciones, name='leerCanciones'),  # views.leer_albumes
    path('leerCancionesPop/', leer_cancionesPop, name='leerCancionesPop'),  # views.leer_albumes
    path('leerCancionesReggaeton/', leer_cancionesReggaeton, name='leerCancionesReggaeton'),  # views.leer_albumes
    path('leerArtistas/', leer_artistas, name='leerArtistas'),  # views.leer_albumes
    path('leerArtistasPop/', leer_artistasPop, name='leerArtistasPop'),  # views.leer_albumes
    path('leerArtistasReggaeton/', leer_artistasReggaeton, name='leerArtistasReggaeton'),  # views.leer_albumes
    
    

    path('album_eliminar/<int:pk>/', AlbumDeleteView.as_view(), name='eliminar_album'),  # eliminar.eliminar_album.AlbumDeleteView
    path('albumPop_eliminar/<int:pk>/', AlbumDeleteViewPop.as_view(), name='eliminar_albumPop'),  # eliminar.eliminar_album.AlbumDeleteView
    path('albumReggaeton_eliminar/<int:pk>/', AlbumDeleteViewReggaeton.as_view(), name='eliminar_albumReggaeton'),  # eliminar.eliminar_album.AlbumDeleteView
    path('eliminar_artista/<int:pk>/', ArtistaDeleteView.as_view(), name='eliminar_artista'),  # eliminar.eliminar_artista.ArtistaDeleteView
    path('eliminar_artistaPop/<int:pk>/', ArtistaDeleteViewPop.as_view(), name='eliminar_artistaPop'),  # eliminar.eliminar_artista.ArtistaDeleteView
    path('eliminar_artistaReggaeton/<int:pk>/', ArtistaDeleteViewReggaeton.as_view(), name='eliminar_artistaReggaeton'),  # eliminar.eliminar_artista.ArtistaDeleteView
    path('eliminar_cancion/<int:pk>/', CancionDeleteView.as_view(), name='eliminar_cancion'),
    path('eliminar_cancionPop/<int:pk>/', CancionDeleteViewPop.as_view(), name='eliminar_cancionPop'),
    path('eliminar_cancionReggaeton/<int:pk>/', CancionDeleteViewReggaeton.as_view(), name='eliminar_cancionReggaeton'),

    
    path('editarAlbum/<int:pk>/', AlbumUpdateView.as_view(), name='album_update'),
    path('editarAlbumPop/<int:pk>/', AlbumUpdateViewPop.as_view(), name='albumPop_update'),
    path('editarAlbumReggaeton/<int:pk>/', AlbumUpdateViewReggaeton.as_view(), name='albumReggaeton_update'),
    path('editarCancion/<int:pk>/', CancionUpdateView.as_view(), name='cancion_update'),
    path('editarCancionPop/<int:pk>/', CancionUpdateViewPop.as_view(), name='cancionPop_update'),
    path('editarCancionReggaeton/<int:pk>/', CancionUpdateViewReggaeton.as_view(), name='cancionReggaeton_update'),
    path('editarArtista/<int:pk>/', ArtistaUpdateView.as_view(), name='artista_update'),
    path('editarArtistaPop/<int:pk>/', ArtistaUpdateViewPop.as_view(), name='artistaPop_update'),
    path('editarArtistaReggaeton/<int:pk>/', ArtistaUpdateViewReggaeton.as_view(), name='artistaReggaeton_update'),

    path('albumDetail/<int:pk>/', AlbumDetailView.as_view(), name='album_detail'),
    path('albumDetailPop/<int:pk>/', AlbumDetailViewPop.as_view(), name='albumPop_detail'),
    path('albumDetailReggaeton/<int:pk>/', AlbumDetailViewReggaeton.as_view(), name='albumReggaeton_detail'),
    path('artistaDetail/<int:pk>/', ArtistaDetailView.as_view(), name='artista_detail'),
    path('artistaDetailPop/<int:pk>/', ArtistaDetailViewPop.as_view(), name='artistaPop_detail'),
    path('artistaDetailReggaeton/<int:pk>/', ArtistaDetailViewReggaeton.as_view(), name='artistaReggaeton_detail'),
    path('cancionDetail/<int:pk>/', CancionDetailView.as_view(), name='cancion_detail'),
    path('cancionDetailPop/<int:pk>/', CancionDetailViewPop.as_view(), name='cancionPop_detail'),
    path('cancionDetailReggaeton/<int:pk>/', CancionDetailViewReggaeton.as_view(), name='cancionReggaeton_detail'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

