from pickle import TRUE
from django.db import models

# Create your models here.
# Esto es para generar las tablas en sqlite


#Clase cliente con atributos
class Clientes(models.Model):
    run=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=21)
    apellido_paterno=models.CharField(max_length=21)
    apellido_materno=models.CharField(max_length=21)
    fecha_nacimiento=models.CharField(max_length=70)
    sexo = models.CharField(max_length=20)

    def __str__(self):
        texto = "{0} {1} {2} {3} {4} {5}"
        return texto.format(self.run, self.nombre, self.apellido_paterno, self.apellido_materno,self.fecha_nacimiento, self.sexo)

#Clase Tipo Calidad (usabilidad, accesibilidad.. ) con sus atributos
class TipoCalidad(models.Model):
    nombre = models.CharField(max_length = 20)

    def __str__(self):
        return self.nombre

#Clase de preguntas del cuestionario
class PreguntasCalidad(models.Model):
    nombre = models.TextField()
    tipo_calidad = models.ForeignKey(TipoCalidad, on_delete=models.CASCADE)
    fecha = models.DateTimeField('date published')
    estado = models.CharField(max_length = 8, default = 'ACTIVO')
    ticket = models.IntegerField(default = 1)

    def __str__(self):
        
        return self.nombre
