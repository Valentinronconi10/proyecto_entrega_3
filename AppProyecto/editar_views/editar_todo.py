from django.views.generic import UpdateView
from AppProyecto.models import *
from django.urls import reverse_lazy
from AppProyecto.forms import CancionFormulario
class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['titulo', 'artista', 'fecha_lanzamiento', 'genero', 'imagen']
    template_name = 'AppProyecto/editar/album_update.html'
    success_url = reverse_lazy('leerAlbumes')



class AlbumUpdateViewPop(UpdateView):
    model = AlbumPop
    fields = ['titulo', 'artista', 'fecha_lanzamiento', 'genero', 'imagen']
    template_name = 'AppProyecto/editar/albumPop_update.html'
    success_url = reverse_lazy('leerAlbumesPop')

class AlbumUpdateViewReggaeton(UpdateView):
    model = AlbumReggaeton
    fields = ['titulo', 'artista', 'fecha_lanzamiento', 'genero', 'imagen']
    template_name = 'AppProyecto/editar/albumReggaeton_update.html'
    success_url = reverse_lazy('leerAlbumesReggaeton')

class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = ['nombre', 'fecha_nacimiento', 'nacionalidad','imagen']
    template_name = 'AppProyecto/editar/artista_update.html'
    success_url = '/artistas/'

class ArtistaUpdateViewPop(UpdateView):
    model = ArtistaPop
    fields = ['nombre', 'fecha_nacimiento', 'nacionalidad','imagen']
    template_name = 'AppProyecto/editar/artistaPop_update.html'
    success_url = '/artistas/'

class ArtistaUpdateViewReggaeton(UpdateView):
    model = ArtistaReggaeton
    fields = ['nombre', 'fecha_nacimiento', 'nacionalidad','imagen']
    template_name = 'AppProyecto/editar/artistaReggaeton_update.html'
    success_url = '/artistas/'

class CancionUpdateView(UpdateView):
    model = Cancion
    form_class = CancionFormulario
    template_name = 'AppProyecto/editar/cancion_update.html'
    success_url = reverse_lazy('leerCanciones')

class CancionUpdateViewPop(UpdateView):
    model = CancionPop
    form_class = CancionFormulario
    template_name = 'AppProyecto/editar/cancionPop_update.html'
    success_url = reverse_lazy('leerCancionesPop')

class CancionUpdateViewReggaeton(UpdateView):
    model = CancionReggaeton
    form_class = CancionFormulario
    template_name = 'AppProyecto/editar/cancionReggaeton_update.html'
    success_url = reverse_lazy('leerCancionesReggaeton')