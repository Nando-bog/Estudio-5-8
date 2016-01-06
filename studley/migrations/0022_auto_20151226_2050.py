# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 01:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studley', '0021_auto_20151226_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColeccionesImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='coleccion',
            name='nombre_corto',
            field=models.SlugField(help_text='Debe ser único.', max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='coleccion',
            name='herramientas_base',
            field=models.ManyToManyField(blank=True, through='studley.ColeccionesHerramientasBase', to='studley.HerramientaBase'),
        ),
        migrations.AddField(
            model_name='coleccionesimagenes',
            name='coleccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Coleccion'),
        ),
        migrations.AddField(
            model_name='coleccionesimagenes',
            name='imagen_coleccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
        ),
        migrations.AddField(
            model_name='coleccion',
            name='imagenes',
            field=models.ManyToManyField(blank=True, through='studley.ColeccionesImagenes', to='studley.Imagen'),
        ),
    ]
