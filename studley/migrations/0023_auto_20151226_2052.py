# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0022_auto_20151226_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coleccion',
            name='nombre_corto',
            field=models.SlugField(help_text='Debe ser único.', max_length=30, unique=True),
        ),
    ]