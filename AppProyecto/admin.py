from django.contrib import admin
from .models import *
from .views import Avatar
# Register your models here.

admin.site.register(Album)
admin.site.register(Cancion)
admin.site.register(Artista)
admin.site.register(Avatar)
admin.site.register(AlbumReggaeton)
admin.site.register(AlbumPop)