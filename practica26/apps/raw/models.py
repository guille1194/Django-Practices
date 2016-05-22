from django.db import models

class Student(models.Model):
	student_code=models.IntegerField()
	student_name=models.CharField(max_length=30)
	student_age=models.IntegerField()
	student_semester=models.IntegerField()

	def __unicode__(self):
		return 'Student code: %d - Student name: %s Student Age: %d- Student semester: %s'%(self.student_code,self.student_name,self.student_age,self.student_semester)
