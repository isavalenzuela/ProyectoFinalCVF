from django.urls import path
from . import views

#URLConf for this app

urlpatterns = [
    path('hello/', views.say_hello)
]