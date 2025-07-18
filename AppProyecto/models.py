from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    titulo= models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_lanzamiento= models.DateField()
    genero = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'albumes_fotos', null= True, blank = True)
    

    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.fecha_lanzamiento} - {self.genero}"
    


class AlbumReggaeton(models.Model):
    titulo= models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_lanzamiento= models.DateField()
    genero = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'albumes_fotos', null= True, blank = True)
    

    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.fecha_lanzamiento} - {self.genero}"
    


class AlbumPop(models.Model):
    titulo= models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_lanzamiento= models.DateField()
    genero = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'albumes_fotos', null= True, blank = True)
    

    def __str__(self):
        return f"{self.titulo} - {self.artista} - {self.fecha_lanzamiento} - {self.genero}"
    



class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    artista = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'canciones_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.titulo} - {self.duracion} - {self.artista} "
    

class CancionPop(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    artista = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'canciones_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.titulo} - {self.duracion} - {self.artista} "
    

class CancionReggaeton(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    artista = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to= 'canciones_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.titulo} - {self.duracion} - {self.artista} "

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'artistas_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_nacimiento} - {self.nacionalidad} "
    
class ArtistaPop(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'artistas_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_nacimiento} - {self.nacionalidad} "

class ArtistaReggaeton(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to= 'artistas_fotos', null= True, blank = True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha_nacimiento} - {self.nacionalidad} "

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    #subcarpeta avatares de media
    imagen = models.ImageField(upload_to= 'avatares', null= True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    