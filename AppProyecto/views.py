from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from .forms import AlbumFormulario
# Create your views here.


def inicio(request):
    return render(request, "AppProyecto/inicio.html")

def artistas(request):
    return render(request, "AppProyecto/artista.html")

def albumes(request):
    return render(request, "AppProyecto/album.html")

def canciones(request):
    return render(request, "AppProyecto/cancion.html")

def crear_formulario(request):
    return render(request, "AppProyecto/crear_formulario.html")

def AlbumFormulario(request):
    if request.method == 'POST':
        formulario = AlbumFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            album = Album(titulo=informacion['titulo'], artista=informacion['artista'], fecha_lanzamiento=informacion['fecha_lanzamiento'])
            album.save()
            return render(request, "AppProyecto/album.html")
    else:
        formulario = AlbumFormulario()
    return render(request, "AppProyecto/crear_formulario.html", {'formulario': formulario})