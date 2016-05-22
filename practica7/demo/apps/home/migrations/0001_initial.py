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
                ('genero', models.CharField(max_length=1)),
                ('perfil_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('perfil_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
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
                ('curso', models.ForeignKey(to='home.Cursos')),
                ('perfil_usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
