from django.conf.urls import url
from .views import index_view, nosotros_view, Registro, cursos_view, talleres_view, aplicacion_view, Registrar_Curso, Registrar_Paciente, Registrar_Profesionista

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^registros$', Registro.as_view(), name = "registros_view"),
    url(r'^$', index_view, name='index_view'),
	url(r'^nosotros/$', nosotros_view, name='nosotros_view'),
	url(r'^cursos/$', cursos_view, name='cursos_view'),
	url(r'^talleres/$', talleres_view, name='talleres_view'),
	url(r'^aplicacion/$', aplicacion_view, name='aplicacion_view'),
    url(r'^Registrar_Profesionista/$', Registrar_Profesionista.as_view(), name ='registrar_profesionista_view'),
	url(r'^Registrar_Paciente/$', Registrar_Paciente.as_view(), name='registrar_paciente_view'),
    url(r'^Registrar_Curso/$', Registrar_Curso.as_view(), name='registrar_curso_view'),
    ]
