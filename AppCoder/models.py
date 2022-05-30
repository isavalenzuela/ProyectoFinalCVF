from statistics import mode
from django.db import models

# Create your models here.


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    anios_exp = models.IntegerField()


class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Profesional(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=1000)
    # foreign key, modificar el modelo y luego migrarlo, relacion de uno a muchos
    especialidad = models.ForeignKey(
        Especialidad, null=False, blank=False, on_delete=models.CASCADE)


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=500)

# relaciones de muchos a muchos, tabla interna que hace django
