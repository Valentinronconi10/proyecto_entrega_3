from django.views.generic import DeleteView
from AppProyecto.models import Cancion

class CancionDeleteView(DeleteView):
    model = Cancion
    template_name = 'AppProyecto/eliminar/cancion_delete.html'
    success_url = '/leerCanciones/'
