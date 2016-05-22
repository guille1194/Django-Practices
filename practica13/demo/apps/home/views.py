from django.shortcuts import render
from .models import Paciente, Profesionista, Horarios, Cursos, ProfesionistaPaciente, HorarioProfesionista
from django.views.generic import CreateView, UpdateView
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

class actualizar_profesionista(UpdateView):
    model = Profesionista
    fields = '__all__'
    template_name = 'home/actualizar_profesionista.html'
    success_url = reverse_lazy('index_view')

class actualizar_paciente(UpdateView):
    model = Paciente
    fields = '__all__'
    template_name = 'home/actualizar_paciente.html'
    success_url = reverse_lazy('index_view')

class actualizar_curso(UpdateView):
    model = Cursos
    fields = '__all__'
    template_name = 'home/actualizar_curso.html'
    success_url = reverse_lazy('index_view')

class actualizar_horario(UpdateView):
    model = Horarios
    fields = '__all__'
    template_name = 'home/actualizar_horario.html'
    success_url = reverse_lazy('index_view')
