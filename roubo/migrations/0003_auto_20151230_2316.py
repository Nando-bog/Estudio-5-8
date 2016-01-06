# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 04:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roubo', '0002_auto_20151229_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='fecha_actualizacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='recurso',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]