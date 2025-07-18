from django.views.generic import DeleteView
from AppProyecto.models import *
from django.urls import reverse_lazy


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'AppProyecto/eliminar/album_delete.html'
    success_url = reverse_lazy('leerAlbumes')

class AlbumDeleteViewPop(DeleteView):
    model = AlbumPop
    template_name = 'AppProyecto/eliminar/albumPop_delete.html'
    success_url = reverse_lazy('leerAlbumesPop')

class AlbumDeleteViewReggaeton(DeleteView):
    model = AlbumReggaeton
    template_name = 'AppProyecto/eliminar/albumReggaeton_delete.html'
    success_url = reverse_lazy('leerAlbumesReggaeton')

class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'AppProyecto/eliminar/artista_delete.html'
    success_url = '/leerArtistas/'

class ArtistaDeleteViewPop(DeleteView):
    model = ArtistaPop
    template_name = 'AppProyecto/eliminar/artistaPop_delete.html'
    success_url = '/leerArtistasPop/'

class ArtistaDeleteViewReggaeton(DeleteView):
    model = ArtistaReggaeton
    template_name = 'AppProyecto/eliminar/artistaReggaeton_delete.html'
    success_url = '/leerArtistasReggaeton/'

class CancionDeleteView(DeleteView):
    model = Cancion
    template_name = 'AppProyecto/eliminar/cancion_delete.html'
    success_url = '/leerCanciones/'


class CancionDeleteViewPop(DeleteView):
    model = CancionPop
    template_name = 'AppProyecto/eliminar/cancionPop_delete.html'
    success_url = '/leerCancionesPop/'

class CancionDeleteViewReggaeton(DeleteView):
    model = CancionReggaeton
    template_name = 'AppProyecto/eliminar/cancionReggaeton_delete.html'
    success_url = '/leerCancionesReggaeton/'