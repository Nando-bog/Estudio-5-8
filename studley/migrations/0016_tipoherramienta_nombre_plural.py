# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0015_remove_marca_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoherramienta',
            name='nombre_plural',
            field=models.CharField(default='nombre_corto', max_length=150),
            preserve_default=False,
        ),
    ]
