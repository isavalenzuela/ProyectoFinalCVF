from django.shortcuts import render
from django.http import HttpResponse
#from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
# this is a request handler
# request -> response

# Create your views here.

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})
