from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify

class Cursos(models.Model):
    numero_curso = models.IntegerField(unique=True)
    curso = models.CharField(max_length=50)

    def __str__(self):
        return self.curso

class Profesionista(models.Model):
    perfil_usuario = models.OneToOneField(User)
    nombre_profesionista = models.CharField(max_length = 68)
    apellido_profesionista = models.CharField(max_length = 68)
    reportes = models.CharField(max_length = 2)
    horario = models.CharField(max_length=50)
    telefono = models.IntegerField()
    curso = models.ForeignKey(Cursos)
    email = models.EmailField()

    def __unicode__(self):
        return(self.curso)

    def __str__(self):
        return 'nombre: %s - curso: %s' %(self.nombre_profesionista, self.curso)

class Paciente(models.Model):
    perfil_usuario = models.OneToOneField(User)
    nombre_paciente = models.CharField(max_length = 99)
    apellido_paciente = models.CharField(max_length = 99)
    num_expediente = models.IntegerField()
    area = models.CharField(max_length = 30)
    fecha_ingreso = models.DateField(default=timezone.now)
    fecha_conclusion = models.DateField(default=timezone.now)
    evaluacion_completa = models.CharField(max_length = 2)
    reportes = models.CharField(max_length = 2)
    diagnostico = models.CharField(max_length = 45)
    fecha_nacimiento = models.DateField(default=timezone.now)
    edad_ingreso = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    genero = models.CharField(max_length=1)


    def __str__(self):
        return 'nombre: %s - numero expediente: %d - edad ingreso: %d' %(self.nombre_paciente, num_expediente, edad_ingreso)

class Perfil(models.Model):
	perfil_usuario = models.OneToOneField(User)
	email = models.EmailField()
