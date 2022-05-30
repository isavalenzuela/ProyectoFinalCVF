from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from AppCoder.models import Contacto, Especialidad, Profesional
#from AppCoder.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
# this is a request handler
# request -> response

# Create your views here.


def bienvenida(request):
    return render(request, "bienvenida.html")


def profesionales(request):
    return render(request, "profesionales.html")


def registraProfesional(request):
    return render(request, "registraProfesionales.html")


def acerca(request):
    return render(request, "acerca.html")


def contactanos(request):
    return render(request, "contactanos.html")


def recibeDatosContacto(request):
    nombre = request.POST['nombre']
    correo = request.POST['correo']
    telefono = request.POST['telefono']
    mensaje = request.POST['mensaje']

    contacto = Contacto(nombre=nombre, correo=correo,
                        telefono=telefono, mensaje=mensaje)
    contacto.save()

    return render(request, "contactanos.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user:
                print('entre al if logueado')
                login(request, user)
                return render(request, "bienvenida.html", {'mensaje': f"Bienvenid@ {user}"})

        else:
            return render(request, "AppCoder/inicio.html", {'mensaje': "Error. Datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form': form})


def lista_profesionales(request):
    if request.method == 'GET':
        usr_select = request.GET['usrselect']

        profesionales = Profesional.objects.filter(especialidad=usr_select)

        print(profesionales)

        contexto = {
            'profesionales': profesionales
        }

        return render(request, "profesionales.html", contexto)

    return render(request, "profesionales.html", contexto)
