# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0013_auto_20151224_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='logo',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
            preserve_default=False,
        ),
    ]