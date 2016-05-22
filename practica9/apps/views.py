from django.shortcuts import render
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from .forms import User_form
from .models import Perfil

def vista1(request):
	return render(request, 'home/vista1.html')
def vista2(request):
	return render(request, 'home/vista2.html')
def vista3(request):
	return render(request, 'home/vista3.html')
def vista4(request):
	return render(request, 'home/vista4.html')
def vista5(request):
	return render(request, 'home/vista5.html')

class Signup(FormView):
	template_name='home/register_user.html'
	form_class=User_form
	succes_url=reverse_lazy('vista1')

	def form_valid(self, form):
		user=form.save()
		p=Perfil()
		p.user_profile=user
		p.mail=form.cleaned_data['mail']
		p.phone=form.cleaned_data['phone']
		p.save()
		return super(Signup, self).form_valid(form)
# Create your views here.
