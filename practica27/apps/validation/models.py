from django.db import models

# Create your models here.
class player(models.Model):
	jugador1=models.CharField(max_length=64)
	jugador2=models.CharField(max_length=64)
	jugador3=models.CharField(max_length=64)

	def __unicode__(self):
		return 'Jugador 1: %s - Jugador 2: %s - Jugador 3: %s'%(self.jugador1,self.jugador2,self.jugador3)
