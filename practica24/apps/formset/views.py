from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView, ListView, DetailView

from .models import chef
from .forms import chefFormSet
from django.core.urlresolvers import reverse_lazy

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.forms.formsets import formset_factory
# Create your views here.
def index_view(request):
	return render(request,'formset/index.html')

#class Datos_register(CreateView):
#	template_name = 'formset/datos.html'
#	model = chef
	#form_class = Personas_Form
#	fields = '__all__'
#	success_url = reverse_lazy('index_view')

class DatosFormSet(FormView):
	template_name = 'formset/datos.html'
	form_class = formset_factory(chefFormSet, extra=2)
	success_url = '//'

	def form_valid(self, form):
		for f in form:
			f.save()
		return super(DatosFormSet, self).form_valid(form)