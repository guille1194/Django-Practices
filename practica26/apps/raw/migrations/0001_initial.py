# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_code', models.IntegerField()),
                ('student_name', models.CharField(max_length=30)),
                ('student_age', models.IntegerField()),
                ('student_semester', models.IntegerField()),
            ],
        ),
    ]
