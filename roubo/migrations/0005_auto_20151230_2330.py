# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-31 04:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roubo', '0004_destacado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destacado',
            name='orden',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]