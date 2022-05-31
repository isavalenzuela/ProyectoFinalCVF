from django.urls import path
from . import views

# URLConf for this app

urlpatterns = [
    path('', views.bienvenida),
    path('profesionales', views.profesionales),
    path('registraProfesionales', views.registraProfesional),
    path('acerca', views.acerca),
    path('contactanos', views.contactanos),
    path('recibeDatosContacto', views.recibeDatosContacto),
    path('login', views.login_request, name='Login'),
    path('listaProfesionales', views.lista_profesionales),
    path('recibeDatosProfesional', views.recibeDatosProfesional)
]
