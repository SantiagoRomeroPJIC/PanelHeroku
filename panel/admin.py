from django.contrib import admin
from .models import Emprendimiento

@admin.register(Emprendimiento)
class EmprendimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dueño', 'lugar', 'fecha_creacion')
    search_fields = ('nombre', 'dueño', 'productos')
    list_filter = ('fecha_creacion',)
    ordering = ('-fecha_creacion',)