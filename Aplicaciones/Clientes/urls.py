from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarClientes),
    path('editarCliente/<run>', views.edicionCliente),
    path('editarCliente/', views.editarCliente),
    path('eliminarCliente/<run>', views.eliminarCliente),
    path('buscaminas', views.buscaminas)
]