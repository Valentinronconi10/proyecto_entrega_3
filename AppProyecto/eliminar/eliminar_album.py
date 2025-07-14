from django.views.generic import DeleteView
from AppProyecto.models import Album

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'AppProyecto/eliminar/album_delete.html'
    success_url = '/leerAlbum/'
