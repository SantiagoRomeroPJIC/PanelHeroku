from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_emprendimientos, name='lista_emprendimientos'),
]
