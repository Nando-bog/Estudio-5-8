# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 04:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0025_auto_20151229_0005'),
    ]

    operations = [
        migrations.AddField(
            model_name='herramienta',
            name='fecha_actualizacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='herramientabase',
            name='fecha_actualizacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='herramientabase',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='marca',
            name='fecha_actualizacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='marca',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tipoherramienta',
            name='fecha_actualizacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='tipoherramienta',
            name='fecha_creacion',
            field=models.DateField(default=datetime.date.today),
        ),
    ]