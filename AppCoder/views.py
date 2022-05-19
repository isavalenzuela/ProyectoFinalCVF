from django.shortcuts import render
from django.http import HttpResponse
#from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
# this is a request handler
# request -> response

# Create your views here.

#def say_hello(request):
#   return render(request, 'hello.html', {'name': 'Mosh'})

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def especialidades(request):
    return render(request, "AppCoder/especialidades.html")

def profesionales(request):
    return render(request, "AppCoder/profesionales.html")

def pacientes(request):
    return render(request, "AppCoder/pacientes.html")