from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import *
from .forms import AlbumFormulario, ArtistaFormulario,CancionFormulario, AvatarForm, EditUserForm, UserRegisterForm
from django.views.generic import  CreateView



from django.db import models
# Create your views here.


def inicio(request):
    return render(request, 'AppProyecto/inicio.html')

def artistas(request):
    return render(request, "AppProyecto/artista.html")

def albumes(request):
    return render(request, "AppProyecto/album.html")




def canciones(request):
    return render(request, "AppProyecto/cancion.html")

def about_me(request):
    return render(request, 'AppProyecto/about_me.html')

def contacto(request):
    return render(request, 'AppProyecto/contacto.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(request, username = usuario, password = contraseña)
            
            if user is not None:
                login(request, user)

        return redirect('inicio')
            
    form =AuthenticationForm()
    return render(request, 'AppProyecto/usuario/login.html', {"form": form})



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'AppProyecto/inicio.html', {"mensaje": "Usuario creado"})
        
    else:
        form = UserRegisterForm()

    return render(request, 'AppProyecto/usuario/registro.html', {"form": form})



def crear_formulario(request):
    return render(request, "AppProyecto/crear_formulario.html")

# def albumFormulario2(request):
#     if request.method == "POST":
#         miFormulario = AlbumFormulario(request.POST)
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#             album = Album(
#                 titulo=informacion["titulo"],
#                 artista=informacion["artista"],
#                 fecha_lanzamiento=informacion["fecha_lanzamiento"],
#             )
#             album.save()
#             return render(request, "AppProyecto/formulario/leer_albumes.html")
#     else:
#         miFormulario = AlbumFormulario()

#     return render(request, "AppProyecto/crear/crear_album.html", {"miFormulario": miFormulario})

# def artistaFormulario(request):
#     if request.method == "POST":
#         miFormulario = ArtistaFormulario(request.POST)
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#             artista = Artista(
#                 nombre=informacion["nombre"],
#                 fecha_nacimiento=informacion["fecha_nacimiento"],
#                 nacionalidad=informacion["nacionalidad"]
#             )
#             artista.save()
#             return render(request, "AppProyecto/artista.html")
#     else:
#         miFormulario = ArtistaFormulario()

#     return render(request, "AppProyecto/formulario/artistaFormulario.html", {"miFormulario": miFormulario})

# def cancionFormulario(request):
#     if request.method == "POST":
#         miFormulario = CancionFormulario(request.POST)
#         if miFormulario.is_valid():
#             informacion = miFormulario.cleaned_data
#             # Aquí tienes un error: estás creando un Artista en vez de una Cancion
#             cancion = Cancion(
#                 titulo=informacion["titulo"],
#                 duracion=informacion["duracion"],
#                 artista=informacion["artista"]
#             )
#             cancion.save()
#             return render(request, "AppProyecto/cancion.html")
#     else:
#         miFormulario = CancionFormulario()

#     return render(request, "AppProyecto/formulario/cancionFormulario.html", {"miFormulario": miFormulario})

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


def leer_albumes(request):
    albumes = Album.objects.all()
    contexto = {"albumes": albumes}
    ordering = ["titulo",]
    return render(request, "AppProyecto/formulario/leer_albumes.html", contexto) 

def leer_albumesPop(request):
    albumes = AlbumPop.objects.all()
    contexto = {"albumes": albumes}
    ordering = ["titulo",]
    return render(request, "AppProyecto/albums/leer_pop.html", contexto) 

def leer_albumesReggaeton(request):
    albumes = AlbumReggaeton.objects.all()
    contexto = {"albumes": albumes}
    ordering = ["titulo",]
    return render(request, "AppProyecto/albums/leer_reggaeton.html", contexto) 


def leer_canciones(request):
    canciones = Cancion.objects.all()
    contexto = {"canciones": canciones}
    ordering = ["titulo",]
    return render(request, "AppProyecto/formulario/leer_canciones.html", contexto)

def leer_cancionesPop(request):
    canciones = CancionPop.objects.all()
    contexto = {"canciones": canciones}
    ordering = ["titulo",]
    return render(request, "AppProyecto/canciones/leer_cancionesPop.html", contexto)

def leer_cancionesReggaeton(request):
    canciones = CancionReggaeton.objects.all()
    contexto = {"canciones": canciones}
    ordering = ["titulo",]
    return render(request, "AppProyecto/canciones/leer_cancionesReggaeton.html", contexto)

def leer_artistas(request):
    artistas = Artista.objects.all()
    contexto = {"artistas": artistas}
    ordering = ["nombre",]
    return render(request, "AppProyecto/formulario/leer_artistas.html", contexto)

def leer_artistasPop(request):
    artistas = ArtistaPop.objects.all()
    contexto = {"artistas": artistas}
    ordering = ["nombre",]
    return render(request, "AppProyecto/artistas/leer_artistasPop.html", contexto)

def leer_artistasReggaeton(request):
    artistas = ArtistaReggaeton.objects.all()
    contexto = {"artistas": artistas}
    ordering = ["nombre",]
    return render(request, "AppProyecto/artistas/leer_artistasReggaeton.html", contexto)

from django.shortcuts import render, redirect
from .forms import AlbumFormulario

# def album_create(request):
#     if request.method == "POST":
#         form = AlbumFormulario(request.POST)
#         if form.is_valid():
#             album = form.save(commit=False)
#             if request.user.is_authenticated:
#                 album.autor = request.user
#                 album.save()
#                 return redirect('leerAlbumes')
#             else:
#                 form.add_error(None, "Debes estar logueado para crear un álbum")
#     else:
#         form = AlbumFormulario()

#     return render(request, "AppProyecto/crear/crear_album.html", context={"form": form})



class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumFormulario
    template_name = 'AppProyecto/crear/crear_album.html'
    success_url = reverse_lazy('leerAlbumes')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear un álbum")
            return self.form_invalid(form)
        return super().form_valid(form)

class ArtistaCreateView(CreateView):
    model = Artista
    form_class = ArtistaFormulario
    template_name = 'AppProyecto/crear/crear_artista.html'
    success_url = reverse_lazy('leerArtistas')

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            form.add_error(None, "Debes estar logueado para crear un artista")
            return self.form_invalid(form)
        return super().form_valid(form)


class CancionCreateView(CreateView):
    model = Cancion
    form_class = CancionFormulario
    template_name = 'AppProyecto/crear/crear_cancion.html'
    success_url = reverse_lazy('leerCanciones')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "Debes estar logueado para crear una cancion")
            return self.form_invalid(form)
        return super().form_valid(form)
    

def perfil(request):
    return render(request, "AppProyecto/usuario/perfil.html")

@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance = request.user)
        try:
            avatar= request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
        
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)

        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user =request.user
            avatar_instance.save()
            messages.success(request,"¡Tus cambios han sido guardados exitosamente!")
            return redirect("perfil")
    else:
        form = EditUserForm(instance = request.user)
        if hasattr(request.user, "avatar"):
            avatar_form = AvatarForm(instance = request.user.avatar)
        else:
            avatar_form = AvatarForm()

    return render(
        request, 'AppProyecto/usuario/editar_perfil.html',  {"form": form, "avatar_form": avatar_form}
    )








