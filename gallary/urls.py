from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('dark/', dark, name='dark'),
    path('album/<int:pk>', album, name='album'),
]