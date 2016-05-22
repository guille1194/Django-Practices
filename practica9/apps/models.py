from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	user_profile=models.OneToOneField(User)
	mail=models.EmailField()
	phone=models.IntegerField()

	def __unicode__(self):
		return self.user_perfil.username
