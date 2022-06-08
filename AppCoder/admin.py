from django.contrib import admin

# Register your models here.

from .models import Profesional, Contacto, UserRegisterForm, Avatar

admin.site.register(Profesional)
admin.site.register(Contacto)
admin.site.register(UserRegisterForm)
admin.site.register(Avatar)
