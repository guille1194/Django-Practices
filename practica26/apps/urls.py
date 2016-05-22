from django.conf.urls import url
from .views import vista1
urlpatterns = [
	url(r'^$', vista1, name='vista1'),
]
