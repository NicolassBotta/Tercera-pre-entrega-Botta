from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import curso, estudiante, profesor
from .forms import Cursoformulario, EstudianteForm, ProfesorForm

# Create your views here.
def crea_curso(req, nombre, camada):

    nuevo_curso = curso(nombre=nombre, camada=camada)

    nuevo_curso.save()
    

    return HttpResponse(f"""
        <p>curso: {nuevo_curso.nombre} - camada: {nuevo_curso.camada} creado</p>
    """)

def lista_cursos(req):
    lista = curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos" : lista})

def inicio(req):

    return render(req, "inicio.html",{})

def cursos(req):

    return render(req, "cursos.html",{})

def estudiantes(req):

    return render(req, "estudiantes.html",{})

def profesores(req):

    return render(req, "profesores.html",{})

def entregables(req):

    return render(req, "entregables.html",{})

def cursoformulario(req):

    if req.method == 'POST':

        miFormulario = Cursoformulario(req.POST) 

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            nuevo_curso = curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()

            return render(req, "inicio.html",{"message": "curso creado con exito"})
        else:
            return render(req, "inicio.html",{"message": "datos invalidos"})
    else:

        miFormulario = Cursoformulario()

        return render(req, "curso_formulario.html",{"miFormulario": miFormulario})
    
    
def busquedacamada(req):

    return render(req, "busquedacamada.html",{})

def buscar(req):

    if req.GET["camada"]:
        
        camada= req.GET["camada"]

        cursos= curso.objects.filter(camada=camada)

        return render(req, "resultadobusqueda.html",{"cursos": cursos, "camada": camada})
    else:
        return render(req, "inicio.html",{"message": "no enviaste el numero de la camada"})


def estudianteformulario(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudianteformulario')
    else:
        form = EstudianteForm()
    return render(request, 'estudianteformulario.html', {'form': form})


def profesorformulario(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesorformulario')
    else:
        form = ProfesorForm()
    return render(request, 'profesorformulario.html', {'form': form})