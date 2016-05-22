from apps.home.models import Paciente

from django.core import serializers
from django.http import HttpResponse

def wsPaciente(request):
	data = serializers.serialize('json', Paciente.objects.all())
	#print data
	return HttpResponse(data, content_type='application/json')
