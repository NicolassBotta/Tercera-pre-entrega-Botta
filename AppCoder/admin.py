from django.contrib import admin

from .models import curso, estudiante, profesor, entregable 
# Register your models here.
admin.site.register(curso)
admin.site.register(estudiante)
admin.site.register(profesor)
admin.site.register(entregable)