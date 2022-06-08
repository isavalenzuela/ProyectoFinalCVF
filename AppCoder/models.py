from statistics import mode
from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


# Create your models here.


class Profesional(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    desc = models.CharField(max_length=1000)
    workplace = models.CharField(max_length=300)
    profRegion = models.CharField(max_length=2)
    especialidad = models.CharField(max_length=50)


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.IntegerField()
    mensaje = models.CharField(max_length=500)


class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir la contraseña', widget=forms.PasswordInput)

    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)


class Avatar(models.Model):
    # vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # subcarpeta avatares de media
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
