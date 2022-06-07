import email
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from AppCoder.models import Contacto, Profesional
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

    contexto = {
        'success': True
    }
    return render(request, "contactanos.html", contexto)


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
        print(usr_select)
        profesionales = Profesional.objects.filter(especialidad=usr_select)

        print(profesionales)

        contexto = {
            'profesionales': profesionales
        }

        return render(request, "profesionales.html", contexto)

    return render(request, "profesionales.html", contexto)


def recibeDatosProfesional(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    desc = request.POST['desc']
    workplace = request.POST['workplace']
    profRegion = request.POST['profRegion']
    profEspecialidad = request.POST['profEspecialidad']

    registroProfesional = Profesional(nombre=nombre, apellido=apellido,
                                      email=email, desc=desc, workplace=workplace, profRegion=profRegion, profEspecialidad=profEspecialidad)
    registroProfesional.save()

    contexto = {
        'success': True
    }

    return render(request, "registraProfesionales.html", contexto)


def cargaDatosProfesional(request, id):
    profesional = Profesional.objects.get(id=id)

    contexto = {
        'profesional': profesional
    }

    return render(request, "editaProfesional.html", contexto)


def executeEditaProfesional(request):
    if request.method == 'POST':
        profesional = Profesional.objects.get(id=request.POST['id'])

        profesional.nombre = request.POST['nombre']
        profesional.apellido = request.POST['apellido']
        profesional.email = request.POST['email']
        profesional.desc = request.POST['desc']
        profesional.workplace = request.POST['workplace']
        profesional.profRegion = request.POST['profRegion']
        profesional.especialidad = request.POST['profEspecialidad']

        profesional.save()

        contexto = {
            'profesional': profesional,
            'success': True
        }

    return render(request, "editaProfesional.html", contexto)


def eliminaProfesional(request):

    contexto = 0

    return render(request, "eliminaProfesional.html", contexto)
