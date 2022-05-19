from django.urls import path
from . import views

#URLConf for this app

urlpatterns = [
    
    path('', views.inicio),
    path('especialidades', views.especialidades),
    path('profesionales', views.profesionales),
    path('pacientes', views.pacientes)
]