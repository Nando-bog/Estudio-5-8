# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0018_tipoherramienta_nombre_plural'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoherramienta',
            name='imagen',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
            preserve_default=False,
        ),
    ]
