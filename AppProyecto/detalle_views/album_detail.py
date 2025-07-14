from django.views.generic import DetailView
from AppProyecto.models import Album

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'AppProyecto/detalle/album_detail.html'
    context_object_name = 'artista'
    