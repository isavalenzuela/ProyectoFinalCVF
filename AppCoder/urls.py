from django.urls import path
from . import views

#URLConf for this app

urlpatterns = [
    path('', views.inicio),
    path('especialidades', views.especialidades),
    path('profesionales', views.profesionales),
    path('pacientes', views.pacientes),
    path('contactanos', views.contactanos),
    path('recibeDatosContacto', views.recibeDatosContacto),
    path('login', views.login_request, name='Login')
]