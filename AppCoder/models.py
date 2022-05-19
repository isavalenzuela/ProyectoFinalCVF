from statistics import mode
from django.db import models

# Create your models here.

class Especialidad(models.Model):
    nombre=models.CharField(max_length=50)
    anios_exp=models.IntegerField()

class Paciente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()

class Profesional(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField()
    especialidad=models.CharField(max_length=50)
    