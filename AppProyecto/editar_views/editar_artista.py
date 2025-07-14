from django.views.generic import UpdateView
from AppProyecto.models import Artista

class ArtistaUpdateView(UpdateView):
    model = Artista
    fields = ['nombre', 'fecha_nacimiento', 'nacionalidad']
    template_name = 'AppProyecto/editar/artista_update.html'
    success_url = '/artistas/'




