# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-23 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0009_auto_20151223_0055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='herramientabase',
            old_name='detalle',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='tipoherramienta',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]
