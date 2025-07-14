from django import forms
from .models import Album, Artista, Cancion, Avatar
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# class AlbumFormulario(forms.Form):
#     class Meta:
#        model= Post
#        titulo = forms.CharField(max_length=100, label='Título del Álbum')
#        artista = forms.CharField(max_length=100, label='Artista')
#        fecha_lanzamiento = forms.DateField(label='Fecha de Lanzamiento', widget=forms.SelectDateWidget(years=range(1900, 2100)))

# class ArtistaFormulario(forms.Form):
#     nombre = forms.CharField(max_length=100, label='Nombre del Artista')
#     fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=range(1900, 2100)))
#     nacionalidad = forms.CharField(max_length=50, label='Nacionalidad')

# class CancionFormulario(forms.Form):
#     titulo = forms.CharField(max_length=100, label='Título de la Canción')
#     duracion = forms.DurationField(label='Duración de la Canción')
#     artista = forms.CharField(max_length=100, label='Artista')
    

class AlbumFormulario(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["titulo", "artista", "fecha_lanzamiento","genero"]

class ArtistaFormulario(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ["nombre", "fecha_nacimiento", "nacionalidad"]

class CancionFormulario(forms.ModelForm):
    class Meta:
        model = Cancion
        fields = ["titulo", "artista", "duracion"]


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']