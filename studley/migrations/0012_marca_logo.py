# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 18:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0011_auto_20151223_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='marca',
            name='logo',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
        ),
    ]
