from django.contrib import admin

# Register your models here.

from .models import Profesional, Contacto

admin.site.register(Profesional)
admin.site.register(Contacto)
