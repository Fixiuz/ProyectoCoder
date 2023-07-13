from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='1981')
    curso.save

    documentodeTexto = f'------>Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(documentodeTexto)
