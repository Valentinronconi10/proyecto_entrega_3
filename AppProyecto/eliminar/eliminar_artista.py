from django.views.generic import DeleteView
from AppProyecto.models import Artista

class ArtistaDeleteView(DeleteView):
    model = Artista
    template_name = 'AppProyecto/eliminar/artista_delete.html'
    success_url = '/leerArtistas/'
