from django.urls import path
from .views import get_maps

app_name = 'maps'

urlpatterns = [
    path('', get_maps, name='hello'),
]