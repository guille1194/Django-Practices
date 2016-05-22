from django.conf.urls import url
from .views import vista1, vista2, vista3, vista4, vista5, Signup

urlpatterns = [

	url(r'^$', vista1, name='vista1'),
	url(r'^vista2$', vista2, name='vista2'),
	url(r'^vista3$', vista3, name='vista3'),
	url(r'^vista4$', vista4, name='vista4'),
	url(r'^vista5$', vista5, name='vista5'),
	url(r'^vista5$', vista5, name='vista5'),
	url(r'^signup/$', Signup.as_view(), name='signup'),
]
