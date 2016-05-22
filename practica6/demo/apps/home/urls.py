from django.conf.urls import url
from .views import home, about, Registros, Reportes, CursoView, ProfesionitaView, admin, PacienteView, ReporteProfesionista, ReportePaciente, ReporteCurso

urlpatterns = [
    url(r'^$', home, name= "home"),
    url(r'^about/$',about, name = "about_view"),
    url(r'^registros$', Registros, name = "registros_view"),
    url(r'^reportes$', Reportes, name = "reportes_view"),
    url(r'^registro_curso$', CursoView.as_view(), name = "CursoView_view" ),
    url(r'^registro_profesionista$',ProfesionitaView.as_view(), name = "ProfesionitaView_view"),
    url(r'^registro_paciente$', PacienteView.as_view(), name = "PacienteView_view"),
    url(r'^ReporteProfesionista/$', ReporteProfesionista.as_view(), name='reporte_profesionista_view'),
	url(r'^ReportePaciente/$', ReportePaciente.as_view(), name='reporte_paciente_view'),
    url(r'^ReporteCurso/$', ReporteCurso.as_view(), name='reporte_curso_view'),
]
