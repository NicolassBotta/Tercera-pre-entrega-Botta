from django import forms


class Cursoformulario(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    

class ProfesorForm(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()