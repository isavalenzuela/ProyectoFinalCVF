from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Contacto
#from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
# this is a request handler
# request -> response

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def especialidades(request):
    return render(request, "especialidades.html")

def profesionales(request):
    return render(request, "profesionales.html")

def pacientes(request):
    return render(request, "pacientes.html")

def contactanos(request):
    return render(request, "contactanos.html")

def recibeDatosContacto(request):
    nombre = request.POST['nombre']
    correo = request.POST['correo']
    telefono = request.POST['telefono']
    mensaje = request.POST['mensaje']

    contacto= Contacto(nombre=nombre,correo=correo, telefono=telefono, mensaje=mensaje)
    contacto.save()
    
    return render(request, "contactanos.html")