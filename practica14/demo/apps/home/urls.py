from django.conf.urls import url
from .views import index_view, nosotros_view, Registro, cursos_view, talleres_view, aplicacion_view

urlpatterns = [
	url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'home/index.html'}, name='login'),
	url(r'^cerrar/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^registros$', Registro.as_view(), name = "registros_view"),
    url(r'^$', index_view, name='index_view'),
	url(r'^nosotros/$', nosotros_view, name='nosotros_view'),
	url(r'^cursos/$', cursos_view, name='cursos_view'),
	url(r'^talleres/$', talleres_view, name='talleres_view'),
	url(r'^aplicacion/$', aplicacion_view, name='aplicacion_view'),
    ]
