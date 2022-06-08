import email
from operator import imod
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from AppCoder.models import Contacto, Profesional, UserRegisterForm, Avatar
# this is a request handler
# request -> response

# Create your views here.


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            avatares = Avatar.objects.filter(user=user)

            contexto = {'mensaje': f"Bienvenid@ {user}",
                        'avatar_url': f"media/{avatares[0].imagen}"}

            if user:
                print('entre al if logueado')
                login(request, user)
                return render(request, "bienvenida.html", contexto)

        else:
            return render(request, "bienvenida.html", {'mensaje': "Error. Datos incorrectos"})
    else:
        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {'form': form})


def register(request):

    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "bienvenida.html", {'mensaje': "Usuari@ Creado"})

    else:
        form = UserRegisterForm()

    return render(request, "registrate.html", {"form": form})


def logout_request(request):
    logout(request)

    return redirect("inicio")


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
                                      email=email, desc=desc, workplace=workplace, profRegion=profRegion, especialidad=profEspecialidad)
    registroProfesional.save()

    contexto = {
        'success': True
    }

    return render(request, "registraProfesionales.html", contexto)


@login_required
def cargaDatosProfesional(request, id):
    profesional = Profesional.objects.get(id=id)

    contexto = {
        'profesional': profesional
    }

    return render(request, "editaProfesional.html", contexto)


@login_required
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


@login_required
def eliminaProfesional(request, id):
    profesional = Profesional.objects.get(id=id)

    contexto = {
        'profesional': profesional,
        'successfulyEliminated': False
    }

    return render(request, "eliminaProfesional.html", contexto)


@login_required
def executeEliminaProfesional(request):

    profesional = Profesional.objects.get(id=request.POST['id'])
    profesional.delete()

    contexto = {
        'successfulyEliminated': True
    }

    return render(request, "eliminaProfesional.html", contexto)
