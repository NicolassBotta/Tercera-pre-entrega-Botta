
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', crea_curso),
    path("listadecursos/", lista_cursos),
        path("inicio/", inicio, name = "Inicio"),
    path("cursos/", cursos, name = "Cursos"),
    path("estudiantes/", estudiantes, name = "Estudiantes"),
    path("profesores/", profesores, name = "Profesores"),
    path("entregables/", entregables, name = "Entregables"),
    path("curso-formulario/", cursoformulario, name = "Formulario"),
    path("busquedacamada/", busquedacamada, name="busquedacamada"),
    path("buscar/", buscar, name="buscar"),
    path('estudianteformulario/', estudianteformulario, name='estudiante_formulario'),
    path('profesorformulario/', profesorformulario, name='profesor_formulario'),
]
