# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0005_auto_20151222_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claseherramienta',
            name='nombre',
            field=models.CharField(choices=[('Acabados', 'Acabados'), ('Afilado', 'Afilado'), ('Alisado', 'Alisado'), ('Atornillado', 'Atornillado'), ('Aseo', 'Aseo'), ('Corte', 'Corte'), ('Labrado', 'Labrado'), ('Marcacion-y-medición', 'Marcación y medición'), ('Perforacion', 'Perforación'), ('Sujecion', 'Sujeción'), ('Golpeo', 'Golpeo'), ('Seguridad', 'Seguridad')], max_length=50, unique=True),
        ),
    ]
