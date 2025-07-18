from AppProyecto.forms import *
from django.views.generic import  CreateView
from AppProyecto.models import *
from django.urls import reverse_lazy


class AlbumCreateViewPop(CreateView):
    model = AlbumPop
    form_class = AlbumFormularioPop
    template_name = 'AppProyecto/crear/crear_albumPop.html'
    success_url = reverse_lazy('leerAlbumesPop')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear un álbum")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class AlbumCreateViewReggaeton(CreateView):
    model = AlbumReggaeton
    form_class = AlbumFormularioReggaeton
    template_name = 'AppProyecto/crear/crear_albumReggaeton.html'
    success_url = reverse_lazy('leerAlbumesReggaeton')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear un álbum")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class ArtistaCreateViewPop(CreateView):
    model = ArtistaPop
    form_class = ArtistaFormularioPop
    template_name = 'AppProyecto/crear/crear_artistaPop.html'
    success_url = reverse_lazy('leerArtistasPop')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "Debes estar logueado para crear un artista")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class ArtistaCreateViewReggaeton(CreateView):
    model = ArtistaReggaeton
    form_class = ArtistaFormularioReggaeton
    template_name = 'AppProyecto/crear/crear_artistaReggaeton.html'
    success_url = reverse_lazy('leerArtistasReggaeton')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "Debes estar logueado para crear un artista")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class CancionCreateViewPop(CreateView):
    model = CancionPop
    form_class = CancionFormularioPop
    template_name = 'AppProyecto/crear/crear_cancionPop.html'
    success_url = reverse_lazy('leerCancionesPop')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear una cancion")
            return self.form_invalid(form)
        return super().form_valid(form)
    
class CancionCreateViewReggaeton(CreateView):
    model = CancionReggaeton
    form_class = CancionFormularioReggaeton
    template_name = 'AppProyecto/crear/crear_cancionReggaeton.html'
    success_url = reverse_lazy('leerCancionesReggaeton')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear una cancion")
            return self.form_invalid(form)
        return super().form_valid(form)