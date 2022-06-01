from django.contrib import admin
from.models import Estudiante
from.models import DeclaracionGanancia
from.models import DeclaracionPerdida

admin.site.register(Estudiante)
admin.site.register(DeclaracionGanancia)
admin.site.register(DeclaracionPerdida)