from django.conf.urls import url
from .views import index_view, nosotros_view, cursos_view, talleres_view, aplicacion_view

urlpatterns = [
    url(r'^$', index_view, name='index_view'),
	url(r'^nosotros/$', nosotros_view, name='nosotros_view'),
	url(r'^cursos/$', cursos_view, name='cursos_view'),
	url(r'^talleres/$', talleres_view, name='talleres_view'),
	url(r'^aplicacion/$', aplicacion_view, name='aplicacion_view'),
    ]
