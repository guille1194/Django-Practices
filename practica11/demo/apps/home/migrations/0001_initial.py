# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero_curso', models.IntegerField(unique=True)),
                ('curso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HorarioProfesionista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('turno', models.CharField(max_length=1, choices=[(b'M', b'Matutino 6:00 - 14:00'), (b'V', b'Vespertino 14:00 - 22:00'), (b'N', b'Nocturno 22:00 - 6:00')])),
                ('curso', models.ForeignKey(to='home.Cursos')),
            ],
            options={
                'ordering': ['curso__numero_curso'],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_paciente', models.CharField(max_length=99)),
                ('apellido_paciente', models.CharField(max_length=99)),
                ('num_expediente', models.IntegerField()),
                ('area', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('fecha_conclusion', models.DateField(default=django.utils.timezone.now)),
                ('evaluacion_completa', models.CharField(max_length=2)),
                ('reportes', models.CharField(max_length=2)),
                ('diagnostico', models.CharField(max_length=45)),
                ('fecha_nacimiento', models.DateField(default=django.utils.timezone.now)),
                ('edad_ingreso', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('genero', models.CharField(max_length=1, choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('perfil_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['perfil_usuario'],
                'permissions': (('puede_ser_paciente', 'Puede ser paciente'),),
            },
        ),
        migrations.CreateModel(
            name='Profesionista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_profesionista', models.CharField(max_length=68)),
                ('apellido_profesionista', models.CharField(max_length=68)),
                ('reportes', models.CharField(max_length=2)),
                ('horario', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('curso', models.ForeignKey(to='home.Cursos')),
                ('perfil_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('puede_hacer_cosas', 'Puede hacer cosas'),),
            },
        ),
        migrations.CreateModel(
            name='ProfesionistaPaciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pacientes', models.ManyToManyField(to='home.Paciente', blank=True)),
                ('profesionista', models.OneToOneField(to='home.Profesionista')),
            ],
        ),
        migrations.AddField(
            model_name='horarioprofesionista',
            name='horario',
            field=models.OneToOneField(to='home.Horarios'),
        ),
        migrations.AddField(
            model_name='horarioprofesionista',
            name='profesionista',
            field=models.ForeignKey(to='home.Profesionista'),
        ),
        migrations.AlterUniqueTogether(
            name='horarios',
            unique_together=set([('curso', 'turno')]),
        ),
    ]
