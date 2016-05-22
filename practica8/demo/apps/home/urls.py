from django.conf.urls import url
from .views import index_view, nosotros_view, cursos_view, talleres_view, aplicacion_view, Registrar_Curso, Registrar_Paciente, Registrar_Horario, Registrar_Profesionista

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
	url(r'^nosotros/$', nosotros_view, name='nosotros_view'),
	url(r'^cursos/$', cursos_view, name='cursos_view'),
	url(r'^talleres/$', talleres_view, name='talleres_view'),
	url(r'^aplicacion/$', aplicacion_view, name='aplicacion_view'),
    url(r'^Registrar_Profesionista/$', Registrar_Profesionista.as_view(), name ='registrar_profesionista_view'),
	url(r'^Registrar_Paciente/$', Registrar_Paciente.as_view(), name='registrar_paciente_view'),
    url(r'^Registrar_Curso/$', Registrar_Curso.as_view(), name='registrar_curso_view'),
    url(r'^Registrar_Horario/$', Registrar_Horario.as_view(), name='registrar_horario_view'),

    ]
