from django import forms

class AlbumFormulario(forms.Form):
    titulo = forms.CharField(max_length=100, label='Título del Álbum')
    artista = forms.CharField(max_length=100, label='Artista')
    fecha_lanzamiento = forms.DateField(label='Fecha de Lanzamiento', widget=forms.SelectDateWidget(years=range(1900, 2100)))
