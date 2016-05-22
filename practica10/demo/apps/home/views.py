from django.shortcuts import render
from .models import Paciente, Profesionista, Horarios, Cursos, ProfesionistaPaciente, HorarioProfesionista
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

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

class Registrar_Curso(CreateView):
	template_name = 'home/Registrar_Cursos.html'
	model = Cursos
	fields = '__all__'
	success_url=reverse_lazy('index_view')

class Registrar_Horario(CreateView):
	template_name = 'home/Registrar_Horarios.html'
	model = Horarios
	fields = '__all__'
	success_url=reverse_lazy('index_view')

class Registrar_Paciente(CreateView):
	template_name='home/Registrar_Paciente.html'
	model = Paciente
	fields= '__all__'
	success_url=reverse_lazy('index_view')

class Registrar_Profesionista(CreateView):
	template_name='home/Registrar_Profesionista.html'
	model = Profesionista
	fields= '__all__'
	success_url=reverse_lazy('index_view')

def buscar_curso(request):
	if request.POST:
		data=request.POST['campo']
		p=Cursos.objects.filter(curso =data)
		ctx={'objects':p}
		print ctx
	else:
		ctx={'mensaje':'No hay datos'}
	return render(request, 'buscar/buscar_curso.html', ctx)

def buscar_paciente(request):
	if request.POST:
		data=request.POST['campo']
		p=Paciente.objects.filter(nombre_paciente =data)
		ctx={'objects':p}
		print ctx
	else:
		ctx={'mensaje':'No hay datos'}
	return render(request, 'buscar/buscar_paciente.html', ctx)

def buscar_profesionista(request):
	if request.POST:
		data=request.POST['campo']
		p=Profesionista.objects.filter(nombre_profesionista =data)
		ctx={'objects':p}
		print ctx
	else:
		ctx={'mensaje':'No hay datos'}
	return render(request, 'buscar/buscar_profesionista.html', ctx)
