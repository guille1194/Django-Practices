from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify
# Create your models here.
class Perfil(models.Model):
	perfil_usuario = models.OneToOneField(User)
	email = models.EmailField()
