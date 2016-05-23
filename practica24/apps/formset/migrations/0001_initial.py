# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='chef',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chef_code', models.IntegerField()),
                ('chef_name', models.CharField(max_length=64)),
                ('chef_age', models.IntegerField()),
                ('chef_area', models.CharField(max_length=64)),
            ],
        ),
    ]
