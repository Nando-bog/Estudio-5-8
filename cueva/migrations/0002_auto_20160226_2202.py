# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cueva', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='destacadohome',
            options={'ordering': ['-orden', '-fecha_creacion'], 'verbose_name': 'Destacado home', 'verbose_name_plural': 'Destacados home'},
        ),
        migrations.AddField(
            model_name='destacadohome',
            name='orden',
            field=models.IntegerField(default=1),
        ),
    ]
