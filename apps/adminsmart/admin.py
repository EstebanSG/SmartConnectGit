from django.contrib import admin

from .models import *

class Eventos_Tabla(admin.ModelAdmin):
    list_display=('titulo', 'fecha')
    model = Eventos

admin.site.register(Eventos, Eventos_Tabla)