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
    workplace = models.CharField(max_length=300)
    profRegion = models.CharField(max_length=2)
    # foreign key, modificar el modelo y luego migrarlo, relacion de uno a muchos
    especialidad = models.ForeignKey(
        Especialidad, null=False, blank=False, on_delete=models.CASCADE)


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=500)

# relaciones de muchos a muchos, tabla interna que hace django

# class Avatar(models.Model):
#     #vinculo con el usuario
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     #subcarpeta avatares de media
#     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
