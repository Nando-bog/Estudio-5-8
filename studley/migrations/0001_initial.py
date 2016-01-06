# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 01:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseHerramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('Acabados', 'Acabados'), ('Afilado', 'Afilado'), ('Alisado', 'Alisado'), ('Atornillado', 'Atornillado'), ('Aseo', 'Aseo'), ('Corte', 'Corte'), ('Labrado', 'Labrado'), ('Marcación y medición', 'Marcación y medición'), ('Perforación', 'Perforación'), ('Sujeción', 'Sujeción'), ('Golpeo', 'Golpeo'), ('Seguridad', 'Seguridad')], max_length=50, unique=True)),
                ('descripcion', models.TextField()),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Clase',
                'verbose_name_plural': 'Clases',
            },
        ),
        migrations.CreateModel(
            name='Coleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('notas', models.TextField(blank=True)),
                ('creador', models.CharField(blank=True, help_text="Diseñador o creador original de esta colección. Ej. Chris Schwarz para ´The Anarchist's Toolchest´. Dejar en blanco si es igual al autor.", max_length=150)),
                ('url', models.URLField(blank=True)),
                ('url_creador', models.URLField(blank=True)),
                ('fecha_creacion', models.DateField()),
                ('fecha_actualizacion', models.DateField()),
                ('autor', models.ForeignKey(help_text='Autor del recurso en el sistema. ', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'Colección',
                'verbose_name_plural': 'Colecciones',
            },
        ),
        migrations.CreateModel(
            name='ColeccionesHerramientas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Coleccion')),
            ],
        ),
        migrations.CreateModel(
            name='ColeccionesHerramientasBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requerida', models.BooleanField(default=True)),
                ('notas', models.TextField(blank=True, help_text='Notas sobre la herramienta en la colección. E.g. Mantener varias cuchillas con distintos radios y ángulos a la mano para este cepillo. ')),
                ('coleccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Coleccion')),
            ],
        ),
        migrations.CreateModel(
            name='Herramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=150)),
                ('detalle', models.TextField(blank=True)),
                ('notas', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Herramienta',
                'verbose_name_plural': 'Herramientas',
            },
        ),
        migrations.CreateModel(
            name='HerramientaBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('nombre_corto', models.SlugField(help_text='Debe ser único.', max_length=30, unique=True)),
                ('detalle', models.TextField(help_text='Describa la herramienta.')),
                ('clase', models.ForeignKey(help_text='Clase de herramienta.', on_delete=django.db.models.deletion.CASCADE, to='studley.ClaseHerramienta')),
            ],
            options={
                'verbose_name': 'Herramienta base',
                'verbose_name_plural': 'Herramientas base',
            },
        ),
        migrations.CreateModel(
            name='HerramientasBaseImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herramienta_base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.HerramientaBase')),
            ],
        ),
        migrations.CreateModel(
            name='HerramientasImagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('herramienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Herramienta')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='herramientas')),
                ('nombre', models.CharField(max_length=150)),
                ('autor', models.CharField(max_length=150)),
                ('url', models.URLField(blank=True)),
                ('licencia', models.TextField()),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imágenes',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('pagina_web', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='TipoHerramienta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.ClaseHerramienta')),
                ('creado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipos',
            },
        ),
        migrations.AddField(
            model_name='herramientasimagenes',
            name='imagen_herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
        ),
        migrations.AddField(
            model_name='herramientasbaseimagenes',
            name='imagen_herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Imagen'),
        ),
        migrations.AddField(
            model_name='herramientabase',
            name='imagenes',
            field=models.ManyToManyField(blank=True, through='studley.HerramientasBaseImagenes', to='studley.Imagen'),
        ),
        migrations.AddField(
            model_name='herramientabase',
            name='tipo',
            field=models.ForeignKey(blank=True, help_text='Tipo o nombre genérico. E.g. Serrucho, el cual es el tipo de ´de corte fino´, ´de costilla´, etc.', on_delete=django.db.models.deletion.CASCADE, to='studley.TipoHerramienta'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='herramienta_base',
            field=models.ForeignKey(help_text='Herramienta genérica de la cual esta es una instancia. E.g. un serrucho de corte fino marca Veritas es una instancia de un Serrucho de corte fino.', on_delete=django.db.models.deletion.CASCADE, to='studley.HerramientaBase'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='imagenes',
            field=models.ManyToManyField(blank=True, through='studley.HerramientasImagenes', to='studley.Imagen'),
        ),
        migrations.AddField(
            model_name='herramienta',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Marca'),
        ),
        migrations.AddField(
            model_name='coleccionesherramientasbase',
            name='herramienta_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.HerramientaBase'),
        ),
        migrations.AddField(
            model_name='coleccionesherramientas',
            name='herramienta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.Herramienta'),
        ),
        migrations.AddField(
            model_name='coleccionesherramientas',
            name='recomendada_para',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studley.ColeccionesHerramientasBase'),
        ),
        migrations.AddField(
            model_name='coleccion',
            name='herramientas_base',
            field=models.ManyToManyField(through='studley.ColeccionesHerramientasBase', to='studley.HerramientaBase'),
        ),
        migrations.AddField(
            model_name='coleccion',
            name='herramientas_recomendadas',
            field=models.ManyToManyField(blank=True, through='studley.ColeccionesHerramientas', to='studley.Herramienta'),
        ),
    ]