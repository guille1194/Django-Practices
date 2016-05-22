from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from .models import Paciente, Profesionista, Cursos, Paciente, Perfil
from django.views.generic import CreateView, FormView
from django.core.urlresolvers import reverse_lazy
from .forms import User_form
from django.core.mail import send_mail
from django.conf import settings

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

class Registro(FormView):
	template_name = 'home/registro.html'
	form_class = User_form
	#fields = ['user_perfil', 'mail', 'phone']
	success_url = reverse_lazy('registros_view')


	def form_valid(self, form):
		user = form.save()
		p = Perfil()
		p.perfil_usuario = user
		p.mail = form.cleaned_data['email']
		p.save()
		return super(Registro, self).form_valid(form)
