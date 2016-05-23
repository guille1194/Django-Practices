from django.db import models

# Create your models here.
class chef(models.Model):
	chef_code = models.IntegerField()
	chef_name = models.CharField(max_length = 64)
	chef_age = models.IntegerField()
	chef_area = models.CharField(max_length = 64)

	def __unicode__(self):
		return 'chef_code: %d - chef_name: %s - chef_age: %d - chef_area: %s'%(self.chef_code, self.chef_name, self.chef_age, self.chef_area)
