from django.urls import path
from .views import inicio, artistas, albumes, canciones

urlpatterns = [
    path('', inicio, name='inicio'),
    path('artistas/', artistas, name='artistas'),
    path('albumes/', albumes, name='albumes'),
    path('canciones/', canciones, name='canciones'),
]