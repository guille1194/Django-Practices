from .models import Paciente
import django
import sys


def imagen_usuario(request):
	try:
		imagen = None
		usuario = request.usuario
		up = Perfil.objects.get(perfil_usuario=usuario)
		#print up
		imagen = 'http://localhost:8000/media/%s'%up.imagen
	except:
		imagen = 'http://localhost:8000/media/debian.jpg'
	return imagen

def myprocessors(request):
	get_version_django = django.get_version()
	get_version_python = sys.version
	p = Student.objects.get(id=1)
	dic = {'valor':p, 'get_image_profile':user_image(request), 'django_version': get_version_django, 'python_version': get_version_python}
	return dic
