from pickle import TRUE
from django.db import models

# Create your models here.

class Clientes(models.Model):
    run=models.CharField(primary_key=True,max_length=11)
    nombre=models.CharField(max_length=21)
    apellido_paterno=models.CharField(max_length=21)
    apellido_materno=models.CharField(max_length=21)
    fecha_nacimiento=models.CharField(max_length=70)
    def __str__(self):
        texto = "{0} {1} {2} {3} {4}"
        return texto.format(self.run, self.nombre, self.apellido_paterno, self.apellido_materno,self.fecha_nacimiento)