from django.db import models

# Create your models here.
class StudentQuerySet(models.QuerySet):

	def etapa_formativa(self, semestre):
		return self.filter(student_semester__lt=semestre)

	def adulto(self, age):
		return self.filter(student_age__gt=age)

class Student(models.Model):
	student_code=models.IntegerField()
	student_name=models.CharField(max_length=30)
	student_age=models.IntegerField()
	student_semester=models.IntegerField()
	objects=StudentQuerySet.as_manager()

	def __unicode__(self):
		return 'Student code: %d - Student name: %s Student Age: %d- Student semester: %s'%(self.student_code,self.student_name,self.student_age,self.student_semester)
