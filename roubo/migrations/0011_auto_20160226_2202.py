# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 03:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roubo', '0010_auto_20160121_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recurso',
            options={'ordering': ['nombre_corto'], 'verbose_name': 'Recurso', 'verbose_name_plural': 'Recursos'},
        ),
    ]
