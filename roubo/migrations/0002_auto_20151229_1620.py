# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 21:20
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('roubo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='Lista de tags separados por comas.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
