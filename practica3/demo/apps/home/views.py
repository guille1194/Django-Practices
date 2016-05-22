from django.shortcuts import render

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
