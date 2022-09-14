from pickle import FALSE
from sqlite3 import IntegrityError
from warnings import catch_warnings
from django.shortcuts import render, redirect
from .models import Clientes
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
import json
from .models import PreguntasCalidad

# Create your views here.


#Vista de inicio, iniciar sesion es requerido para visualizar las vistas
@login_required
def home(request):
    clientes = Clientes.objects.all()
    return render(request, "gestionClientes.html", {"clientes": clientes})

#Registrar cliente recibe un post del formulario en gestionClientes.html para guardar los datos de cada cliente en la base de datos
@login_required
def registrarClientes(request):
    run = request.POST['txtRun']
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtAPaterno']
    apellido_materno = request.POST['txtAM']
    fecha_nacimiento = request.POST['txtDate']
    sexo = request.POST['sexo']

    try:
        cliente = Clientes.objects.create(run=run, nombre=nombre,apellido_paterno=apellido_paterno, apellido_materno=apellido_materno, fecha_nacimiento=fecha_nacimiento, sexo=sexo)
        messages.success(request, 'Cliente guardado correctamente')
        return redirect('/')
    except IntegrityError as e:
        if 'UNIQUE constraint' in e.args:
            messages.error(request,'Error')
        return redirect('/')

#Se elimina un cliente en la base de datos
@login_required
def eliminarCliente(request, run):
    cliente = Clientes.objects.get(run=run)
    cliente.delete()
    return redirect('/')

@login_required
def edicionCliente(request, run):
    cliente = Clientes.objects.get(run=run)
    return render(request, "editarCliente.html", {"cliente": cliente})

@login_required
def editarCliente(request):
    run = request.POST['txtRun']
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtAPaterno']
    apellido_materno = request.POST['txtAM']
    fecha_nacimiento = request.POST['txtDate']
    sexo = request.POST['sexo']

    cliente = Clientes.objects.get(run=run)
    cliente.nombre = nombre
    cliente.apellido_paterno = apellido_paterno
    cliente.apellido_materno = apellido_materno
    cliente.fecha_nacimiento = fecha_nacimiento
    cliente.sexo = sexo
    cliente.save()
    return redirect('/')

@login_required
def buscaminas(request):
    return render(request, "buscaminas.html")

@login_required
def login(request):
    return render(request, "registration/login.html")

@login_required
def salir(request):
    logout(request)
    return redirect('/')

@login_required
def calculadora(request):
    return render(request, "calculadora.html")


#Peticion que obtiene las preguntas del cuestionario filtrada por tipo calidad
@login_required
def json(request,tp):
    tipo = PreguntasCalidad.objects.filter(tipo_calidad=tp)
    data = list(tipo.values())
    return JsonResponse(data,safe = False)

@login_required
def preguntas(request):
    return render(request, "cuestionario.html")

@login_required
def tickets(request):
    ticket_true = PreguntasCalidad.objects.filter(ticket=1).count()
    ticket_false = PreguntasCalidad.objects.filter(ticket=0).count()

    ticket_true_acce = PreguntasCalidad.objects.filter(ticket=1, tipo_calidad=1).count()
    ticket_false_acce = PreguntasCalidad.objects.filter(ticket=0, tipo_calidad=1).count()

    ticket_true_usa = PreguntasCalidad.objects.filter(ticket=1, tipo_calidad=2).count()
    ticket_false_usa = PreguntasCalidad.objects.filter(ticket=0, tipo_calidad=2).count()

    ticket_true_seg = PreguntasCalidad.objects.filter(ticket=1, tipo_calidad=3).count()
    ticket_false_seg = PreguntasCalidad.objects.filter(ticket=0, tipo_calidad=3).count()

    ticket_true_rda = PreguntasCalidad.objects.filter(ticket=1, tipo_calidad=4).count()
    ticket_false_rda = PreguntasCalidad.objects.filter(ticket=0, tipo_calidad=4).count()

    data =  [{'ticket_true': ticket_true, 
        'ticket_false': ticket_false,
        'ticket_true_acce': ticket_true_acce,
        'ticket_false_acce': ticket_false_acce,
        'ticket_true_usa': ticket_true_usa,
        'ticket_false_usa': ticket_false_usa,
        'ticket_true_seg': ticket_true_seg,
        'ticket_false_seg': ticket_false_seg,
        'ticket_true_rda': ticket_true_rda,
        'ticket_false_rda': ticket_false_rda

        }]
    return JsonResponse(data, safe=False)

@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def sexo(request):
    masculino = Clientes.objects.filter(sexo='Masculino').count()
    femenino = Clientes.objects.filter(sexo='Femenino').count()
    Otro = Clientes.objects.filter(sexo='Prefiere no decir').count()

    data = [{
        'masculino': masculino,
        'femenino' : femenino,
        'otro' : Otro
    }]

    return JsonResponse(data, safe=False)

