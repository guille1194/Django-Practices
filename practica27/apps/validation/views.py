from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import player
from django.core.urlresolvers import reverse_lazy
# Create your views here.

def vista1(request):
	return render(request, 'validation/vista1.html')

class PlayerReport(ListView):
	template_name='validation/player_report.html'
	model=player

class Register_Player(CreateView):
	template_name='validation/register_player.html'
	model = player
	fields=['jugador1','jugador2','jugador3']
	success_url=reverse_lazy('report_player')

	def post(self, request, *args, **kwargs):
		flag=False
		p=player()
		p.jugador1=request.POST['jugador1']
		p.jugador2=request.POST['jugador2']
		p.jugador3=request.POST['jugador3']
		p.save()
		flag=True
		return render(request, 'validation/register_player.html', {'flag':flag})
