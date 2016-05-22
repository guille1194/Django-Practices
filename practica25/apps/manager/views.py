from django.shortcuts import render

# Create your views here.
def vista1(request):
	return render(request, 'manager/vista1.html')
