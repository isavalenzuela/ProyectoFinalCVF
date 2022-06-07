from django.urls import path, re_path
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
    path('recibeDatosProfesional', views.recibeDatosProfesional),
    re_path(r'cargaDatos Profesional/(?P<id>[0-9]+)',
            views.cargaDatosProfesional, name='cargaDatosProfesional'),
    path('executeEditaProfesional', views.executeEditaProfesional),
    re_path(r'eliminaProfesional/<int:id>/',
            views.eliminaProfesional, name='eliminaProfesional')
]
