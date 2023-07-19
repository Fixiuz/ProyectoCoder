from django.shortcuts import render
from AppCoder.models import Curso, Profesor,Entregable, Estudiante
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EntregableFormulario, EstudiantesFormulario


# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='1981')
    curso.save

    documentodeTexto = f'------>Curso: {curso.nombre} Camada: {curso.camada}'

    return HttpResponse(documentodeTexto)
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

#def cursos(request):
    # return render(request, 'AppCoder/cursos.html')

def profesores(request):
     return render(request, 'AppCoder/profesores.html')


def estudiantes(request):
     if request.method == 'POST':
          miFormulario = EstudiantesFormulario(request.POST) # aca llega la informacion del html
          print(miFormulario)
          
          if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
               
               estudiante = Estudiante(nombre = informacion['nombre'],
                                        apellido = informacion['apellido'],
                                        email=informacion['email'])
          estudiante.save()
          return render(request, 'Appcoder/inicio.html')
     else:
          miFormulario = EstudiantesFormulario()
     
     return render(request, 'AppCoder/estudiantes.html', {"miFormulario": miFormulario})     




def entregables(request):
     if request.method == 'POST':
          miFormulario = EntregableFormulario(request.POST) # aca llega la informacion del html
          print(miFormulario)
          
          if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
               
               entregable = Entregable(nombre = informacion['nombre'],
                                        fecha_entrega = informacion['fecha_entrega'],
                                        entregado=informacion['entregado'])
          entregable.save()
          return render(request, 'Appcoder/inicio.html')
     else:
          miFormulario = EntregableFormulario()
     
     return render(request, 'AppCoder/entregables.html', {"miFormulario": miFormulario})     

def cursos(request):
     if request.method == 'POST':
          miFormulario = CursoFormulario(request.POST) # aca llega la informacion del html
          print(miFormulario)
          
          if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
               
               curso = Curso(nombre = informacion['nombre'],
                                        camada = informacion['camada'])
          curso.save()
          return render(request, 'Appcoder/inicio.html')
     else:
          miFormulario = CursoFormulario()
     
     return render(request, 'AppCoder/cursos.html', {"miFormulario": miFormulario})

def profesorFormulario(request):
     if request.method == 'POST':
          miFormulario = ProfesorFormulario(request.POST)
          print(miFormulario)

          if miFormulario.is_valid:
               informacion = miFormulario.cleaned_data
               profesor = Profesor (nombre = informacion['nombre'],
                                     apellido = informacion['apellido'],
                                     email=informacion['email'],
                                     profesion=informacion['profesion'])
          profesor.save()
          return render(request,'AppCoder/inicio.html') 
     else:
          miFormulario = ProfesorFormulario()
     return render(request, 'AppCoder/profesorFormulario.html', {'miFormulario': miFormulario})     

def busquedaCamada(request):
     return render(request, 'AppCoder/busquedaCamada.html')

def buscar(request):
     if request.GET['camada']:        
          camada = request.GET['camada']
          cursos = Curso.objects.filter( camada__icontains = camada)
          return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})
     else:
          respuesta = 'No enviaste datos'

     return render (request, 'AppCoder/inicio.html', {'respuesta': respuesta})
     



