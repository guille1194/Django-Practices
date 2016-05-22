from django.shortcuts import render
from .models import Paciente, Profesionista, Horarios, Cursos, ProfesionistaPaciente, HorarioProfesionista
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .forms import Registrar_Cursos_Form, Registrar_Horarios_Form, Registrar_Paciente_Form, Registrar_Profesionista_Form
# Create your views here.
def index_view(request):
    return render(request, 'home/index.html')

def nosotros_view(request):
	return render(request, 'home/nosotros.html')

def cursos_view(request):
	return render(request, 'home/cursos.html')

def talleres_view(request):
	return render(request, 'home/talleres.html')

def aplicacion_view(request):
	return render(request, 'home/aplicacion.html')

def Registrar_Curso(request):
	form = Registrar_Cursos_Form(request.POST)
	ctx = {'form':form }
	if form.is_valid():
		form.save()
		ctx = {'form':form, 'mensaje':'Datos Guardados....'}
	else:
		form = Registrar_Cursos_Form()
		ctx = {'form':form}

	return render(request, 'home/Registrar_Cursos.html',ctx)

def Registrar_Horario(request):
	form = Registrar_Horarios_Form(request.POST)
	ctx = {'form':form }
	if form.is_valid():
		form.save()
		ctx = {'form':form, 'mensaje':'Datos Guardados....'}
	else:
		form = Registrar_Horarios_Form()
		ctx = {'form':form}

	return render(request, 'home/Registrar_Horarios.html',ctx)

def Registrar_Paciente(request):
	form = Registrar_Paciente_Form(request.POST)
	ctx = {'form':form }
	if form.is_valid():
		form.save()
		ctx = {'form':form, 'mensaje':'Datos Guardados....'}
	else:
		form = Registrar_Paciente_Form()
		ctx = {'form':form}

	return render(request, 'home/Registrar_Paciente.html',ctx)

def Registrar_Profesionista(request):
	form = Registrar_Profesionista_Form(request.POST)
	ctx = {'form':form }
	if form.is_valid():
		form.save()
		ctx = {'form':form, 'mensaje':'Datos Guardados....'}
	else:
		form = Registrar_Profesionista_Form()
		ctx = {'form':form}

	return render(request, 'home/Registrar_Profesionista.html',ctx)
