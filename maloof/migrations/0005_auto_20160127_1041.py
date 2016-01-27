# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-27 15:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('maloof', '0004_auto_20160121_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='twitter',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, default=datetime.datetime(2016, 1, 27, 15, 41, 20, 995729, tzinfo=utc)),
        ),
    ]
