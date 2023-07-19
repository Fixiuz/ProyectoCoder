from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()    
    profesion = forms.CharField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField()
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
