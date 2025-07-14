from django.views.generic import UpdateView
from AppProyecto.models import Cancion
from AppProyecto.forms import CancionFormulario
from django.urls import reverse_lazy
class CancionUpdateView(UpdateView):
    model = Cancion
    form_class = CancionFormulario
    template_name = 'AppProyecto/editar/cancion_update.html'
    success_url = reverse_lazy('leerCanciones')
    
