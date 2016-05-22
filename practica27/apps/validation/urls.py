from django.conf.urls import url
from .views import vista1, Register_Player, PlayerReport
urlpatterns = [
	url(r'^$', vista1, name='vista1'),
	url(r'^register_player/$', Register_Player.as_view(), name='register_player'),
	url(r'^report_player$', PlayerReport.as_view(), name='report_player'),
]