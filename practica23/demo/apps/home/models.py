from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.template.defaultfilters import slugify

class Cursos(models.Model):
    numero_curso = models.IntegerField(unique=True)
    curso = models.CharField(max_length=50)
    curso_imagen = models.ImageField(upload_to='curso_imagen/')


    def __unicode__(self):
        return 'Curso %d: %s'%(self.numero_curso,self.curso)

class Profesionista(models.Model):
    perfil_usuario = models.OneToOneField(User)
    nombre_profesionista = models.CharField(max_length = 68)
    apellido_profesionista = models.CharField(max_length = 68)
    reportes = models.CharField(max_length = 2)
    horario = models.CharField(max_length=50)
    telefono = models.IntegerField()
    curso = models.ForeignKey(Cursos)
    email = models.EmailField()

    class Meta:
        permissions = (('puede_hacer_cosas','Puede hacer cosas'),)

    def __str__(self):
        return 'nombre: %s - curso: %s' %(self.nombre_profesionista, self.curso)

class Horarios(models.Model):
    curso = models.ForeignKey(Cursos)
    TURNO = (
            ('M', 'Matutino 6:00 - 14:00'),
            ('V', 'Vespertino 14:00 - 22:00'),
            ('N', 'Nocturno 22:00 - 6:00'),
            )
    turno = models.CharField(max_length=1, choices=TURNO)

    class Meta:
        unique_together = ('curso','turno',)
        ordering = ['curso__numero_curso',]

    def __unicode__(self):
        return '%s - Turn: %s'%(self.curso,self.turno)

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
    ELECCION_GENERO = (
                    ('M', 'Masculino'),
                    ('F', 'Femenino'),
                    )
    genero = models.CharField(max_length=1, choices=ELECCION_GENERO)

    class Meta:
        permissions = (('puede_ser_paciente','Puede ser paciente'),)
        ordering = ['perfil_usuario']

    def __str__(self):
        return 'nombre: %s - numero expediente: %d - edad ingreso: %d' %(self.nombre_paciente, num_expediente, edad_ingreso)

class Perfil(models.Model):
	perfil_usuario = models.OneToOneField(User)
	mail = models.EmailField()
	telefono = models.IntegerField()
	imagen = models.ImageField(upload_to='imagen_usuario', blank=True)

	def thumbnail(self):
		return '<a href="http://localhost:8000/media/%s"><img src="http://localhost:8000/media/%s" width=50px/></a>'%(self.image, self.image)
	thumbnail.allow_tags = True

class ProfesionistaPaciente(models.Model):
	profesionista = models.OneToOneField(Profesionista)
	pacientes = models.ManyToManyField(Paciente, blank=True)

	def __unicode__(self):
		return '%s - %s'%(self.profesionista,self.pacientes)

class HorarioProfesionista(models.Model):
	profesionista = models.ForeignKey(Profesionista)
	horario = models.OneToOneField(Horarios, unique=True)

	def __unicode__(self):
		return '%s - Horario: %s'%(self.profesionista,self.horario)
