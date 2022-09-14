from django.urls import path
from . import views

#Urls del sitio
urlpatterns = [
    path('', views.home),
    path('registrarCliente/', views.registrarClientes),
    path('editarCliente/<run>', views.edicionCliente),
    path('editarCliente/', views.editarCliente),
    path('eliminarCliente/<run>', views.eliminarCliente),
    path('buscaminas', views.buscaminas),
    path('registration/login', views.login),
    path('salir/', views.salir),
    path('calculadora/', views.calculadora),
    path('json/<tp>', views.json),
    path('cuestionario/', views.preguntas),
    path('dashboard/', views.dashboard),
    path('tickets/', views.tickets),
    path('sexo/', views.sexo)

]