from django.contrib import admin
from .models import Avatar, Turnos, Usuarios, models

# Register your models here.

admin.site.register(Usuarios)
admin.site.register(Turnos)
admin.site.register(Avatar)