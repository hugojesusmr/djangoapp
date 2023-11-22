from django.contrib import admin
from django.urls import path
from django import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listarSitios', views.listarSitios, name='listarSitios'),
    path('listarFO', views.listarFO, name='listarFO'),
    path('cargarSitios', views.cargarSitios, name='cargarSitios'),
    path('cargarFO', views.cargarFO, name='cargarFO'),
    path('cargarAGG', views.cargarAGG, name='cargarAGG'),
]