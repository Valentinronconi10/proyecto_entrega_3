from django.views.generic import DetailView
from AppProyecto.models import Cancion

class CancionDetailView(DetailView):
    model = Cancion
    template_name = 'AppProyecto/detalle/cancion_detail.html'
    context_object_name = 'artista'
    