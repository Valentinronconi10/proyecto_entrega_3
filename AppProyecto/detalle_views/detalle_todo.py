from django.views.generic import DetailView
from AppProyecto.models import *

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'AppProyecto/detalle/album_detail.html'
    context_object_name = 'albumes/'

class AlbumDetailViewPop(DetailView):
    model = AlbumPop
    template_name = 'AppProyecto/detalle/albumPop_detail.html'
    context_object_name = 'albumes/'

class AlbumDetailViewReggaeton(DetailView):
    model = AlbumReggaeton
    template_name = 'AppProyecto/detalle/albumReggaeton_detail.html'
    context_object_name = 'albumes/'
    

class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'AppProyecto/detalle/artista_detail.html'
    context_object_name = 'artistas/'
    
class ArtistaDetailViewPop(DetailView):
    model = ArtistaPop
    template_name = 'AppProyecto/detalle/artistaPop_detail.html'
    context_object_name = 'artistas/'

class ArtistaDetailViewReggaeton(DetailView):
    model = ArtistaReggaeton
    template_name = 'AppProyecto/detalle/artistaReggaeton_detail.html'
    context_object_name = 'artistas/'


class CancionDetailView(DetailView):
    model = Cancion
    template_name = 'AppProyecto/detalle/cancion_detail.html'
    context_object_name = 'canciones/'

class CancionDetailViewPop(DetailView):
    model = CancionPop
    template_name = 'AppProyecto/detalle/cancionPop_detail.html'
    context_object_name = 'canciones/'
    

class CancionDetailViewReggaeton(DetailView):
    model = CancionReggaeton
    template_name = 'AppProyecto/detalle/cancionReggaeton_detail.html'
    context_object_name = 'canciones/'
    