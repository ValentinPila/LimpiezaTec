from django.contrib import admin
from .models import *

class ComentarioInLine(admin.StackedInline):
    model = Comentarios

class CursoAdmin(admin.ModelAdmin):
    inlines = [ComentarioInLine]

admin.site.register(Comentarios)
admin.site.register(Tarea)
admin.site.register(Tecnologico)

# Register your models here.
