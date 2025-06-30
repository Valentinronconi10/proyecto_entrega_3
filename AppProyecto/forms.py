from django import forms

class AlbumFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, label='Título del Álbum')
    artista = forms.CharField(max_length=100, label='Artista')
    fecha_lanzamiento = forms.DateField(label='Fecha de Lanzamiento', widget=forms.SelectDateWidget(years=range(1900, 2100)))

class ArtistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del Artista')
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.SelectDateWidget(years=range(1900, 2100)))
    nacionalidad = forms.CharField(max_length=50, label='Nacionalidad')

class CancionFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, label='Título de la Canción')
    duracion = forms.DurationField(label='Duración de la Canción')
    artista = forms.CharField(max_length=100, label='Artista')
    