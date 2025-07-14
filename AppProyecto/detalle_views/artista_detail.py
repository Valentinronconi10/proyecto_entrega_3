from django.views.generic import DetailView
from AppProyecto.models import Artista

class ArtistaDetailView(DetailView):
    model = Artista
    template_name = 'AppProyecto/detalle/artista_detail.html'
    context_object_name = 'artista'
    