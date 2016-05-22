from django.conf.urls import url
from .views import wsPaciente

urlpatterns = [

	url(r'^ws/paciente/$', wsPaciente, name='wsPaciente_view'),
]
