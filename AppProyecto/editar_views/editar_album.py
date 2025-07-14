from django.views.generic import UpdateView
from AppProyecto.models import Album

class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['titulo', 'artista', 'fecha_lanzamiento', 'genero']
    template_name = 'AppProyecto/editar/album_update.html'
    success_url = '/album/'


