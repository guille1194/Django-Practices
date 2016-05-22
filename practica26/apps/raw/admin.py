from django.contrib import admin

# Register your models
from .models import Student

@admin.register(Student)
class Student_admin(admin.ModelAdmin):
	list_display=('student_code','student_name','student_age','student_semester',)
