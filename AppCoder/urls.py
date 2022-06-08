from django.urls import path, re_path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

# URLConf for this app

urlpatterns = [
    path('', views.bienvenida),
    path('profesionales', views.profesionales),
    path('registraProfesionales', views.registraProfesional),
    path('acerca', views.acerca),
    path('contactanos', views.contactanos),
    path('recibeDatosContacto', views.recibeDatosContacto),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(
        template_name='logout.html'), name='Logout'),
    path('listaProfesionales', views.lista_profesionales),
    path('recibeDatosProfesional', views.recibeDatosProfesional),
    re_path(r'cargaDatos Profesional/(?P<id>[0-9]+)',
            views.cargaDatosProfesional, name='cargaDatosProfesional'),
    path('executeEditaProfesional', views.executeEditaProfesional),
    re_path(r'eliminaProfesional/(?P<id>[0-9]+)',
            views.eliminaProfesional, name='eliminaProfesional'),
    path('executeEliminaProfesional', views.executeEliminaProfesional),
]
