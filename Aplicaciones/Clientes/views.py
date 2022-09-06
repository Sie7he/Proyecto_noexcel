from sqlite3 import IntegrityError
from warnings import catch_warnings
from django.shortcuts import render, redirect
from .models import Clientes
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.

@login_required
def home(request):
    clientes = Clientes.objects.all()
    return render(request, "gestionClientes.html", {"clientes": clientes})

def registrarClientes(request):
    run = request.POST['txtRun']
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtAPaterno']
    apellido_materno = request.POST['txtAM']
    fecha_nacimiento = request.POST['txtDate']

    try:
        cliente = Clientes.objects.create(run=run, nombre=nombre,apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, fecha_nacimiento=fecha_nacimiento)
        messages.success(request, 'Cliente guardado correctamente')
        return redirect('/')
    except IntegrityError as e:
        if 'UNIQUE constraint' in e.args:
            messages.error(request,'Error')
        return redirect('/')

def eliminarCliente(request, run):
    cliente = Clientes.objects.get(run=run)
    cliente.delete()
    return redirect('/')

def edicionCliente(request, run):
    cliente = Clientes.objects.get(run=run)
    return render(request, "editarCliente.html", {"cliente": cliente})

def editarCliente(request):
    run = request.POST['txtRun']
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtAPaterno']
    apellido_materno = request.POST['txtAM']
    fecha_nacimiento = request.POST['txtDate']

    cliente = Clientes.objects.get(run=run)
    cliente.nombre = nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.fecha_nacimiento = fecha_nacimiento
    cliente.save()
    return redirect('/')

def buscaminas(request):
    return render(request, "buscaminas.html")

def login(request):
    return render(request, "registration/login.html")

def salir(request):
    logout(request)
    return redirect('/')