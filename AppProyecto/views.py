from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Cancion, Artista
from .forms import AlbumFormulario, ArtistaFormulario, CancionFormulario
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

def albumFormulario2(request):
    if request.method == "POST":
        miFormulario = AlbumFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            album = Album(
                titulo=informacion["titulo"],
                artista=informacion["artista"],
                fecha_lanzamiento=informacion["fecha_lanzamiento"],
            )
            album.save()
            return render(request, "AppProyecto/album.html")
    else:
        miFormulario = AlbumFormulario()

    return render(request, "AppProyecto/formulario/albumFormulario2.html", {"miFormulario": miFormulario})

def artistaFormulario(request):
    if request.method == "POST":
        miFormulario = ArtistaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            artista = Artista(
                nombre=informacion["nombre"],
                fecha_lanzamiento=informacion["fecha_lanzamiento"],
                nacionalidad=informacion["nacionalidad"]
            )
            artista.save()
            return render(request, "AppProyecto/artista.html")
    else:
        miFormulario = ArtistaFormulario()

    return render(request, "AppProyecto/formulario/artistaFormulario.html", {"miFormulario": miFormulario})

def cancionFormulario(request):
    if request.method == "POST":
        miFormulario = CancionFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            # Aquí tienes un error: estás creando un Artista en vez de una Cancion
            cancion = Cancion(
                titulo=informacion["titulo"],
                duracion=informacion["duracion"],
                artista=informacion["artista"]
            )
            cancion.save()
            return render(request, "AppProyecto/cancion.html")
    else:
        miFormulario = CancionFormulario()

    return render(request, "AppProyecto/formulario/cancionFormulario.html", {"miFormulario": miFormulario})

def buscar(request):
    # Verifica que el parámetro "cancion" exista en el GET
    if request.GET.get("cancion"):
        cancion = request.GET["cancion"]
        # Busca canciones cuyo título contenga el texto ingresado (no distingue mayúsculas/minúsculas)
        canciones = Cancion.objects.filter(titulo__icontains=cancion)
        return render(request, "AppProyecto/formulario/resultadoBusqueda.html", {"cancion": cancion, "canciones": canciones})
    else:
        return HttpResponse("No se envió información")

def busquedaCancion(request):
    return render(request, "AppProyecto/formulario/busquedaCancion.html")