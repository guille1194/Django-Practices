from django.conf.urls import url
from .views import index_view,DatosFormSet
urlpatterns = [
	url(r'^$',index_view,name='index_view'),
	url(r'^dato/$', DatosFormSet.as_view(), name='datos_view'),
	
]