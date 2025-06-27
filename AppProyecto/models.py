from django.db import models



class Album(models.Model):
    titulo= models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_lanzamiento= models.DateField()
    genero = models.CharField(max_length=50)

class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    duracion = models.DurationField()
    artista = models.CharField(max_length=100)

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)
    
