# coding=utf-8
# modelos para el home e integracion de otros modelos del proyecto en la página de inicio
# version 0.1
# febrero 26, 2016
import datetime
import os
from uuid import uuid4
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def change_uploaded_filename(instance, filename):
        """Return a path and filename to upload an image."""
        upload_to = "home_image"
        extension = filename.split('.')[-1]
        filename = '{0}.{1}'.format(uuid4().hex, extension)
        return os.path.join(upload_to, filename)


class DestacadoHome(models.Model):
    """Objetos destacados que ese muestran en el home del proyecto."""
    # CONSTANTES
    RECURSOS = models.Q(app_label='roubo', model='recurso')
    TIPOS_HERRAMIENTAS = models.Q(app_label='studley', model='tipoherramienta')
    HERRAMIENTAS_BASE = models.Q(app_label='studley', model='herramientabase')
    HERRAMIENTA = models.Q(app_label='studley', model='herramienta')
    COLECCIONES = models.Q(app_label='studley', model='coleccion')
    DESTACABLES = RECURSOS | TIPOS_HERRAMIENTAS | HERRAMIENTAS_BASE | COLECCIONES

    content_type = models.ForeignKey(ContentType, limit_choices_to=DESTACABLES)
    object_id = models.PositiveIntegerField()
    contenido_destacado = GenericForeignKey('content_type', 'object_id')
    fecha_creacion = models.DateField(default=datetime.date.today)
    orden = models.IntegerField(default=1)

    class Meta:
        ordering = ['-orden', '-fecha_creacion']
        verbose_name_plural = 'Destacados home'
        verbose_name = 'Destacado home'

    def __str__(self):
        return '{0} {1}'.format(self.content_type, self.contenido_destacado)


class ImagenFondoHome(models.Model):
    """Imagen de fondo de la pagina home.
    """
    imagen = models.ImageField(upload_to=change_uploaded_filename)
    nombre = models.CharField(max_length=150, default='sin título')
    autor = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)
    licencia = models.TextField(blank=True)

    class Meta:
        verbose_name = "Imagen inicio"
        verbose_name_plural = "Imágenes inicio"

    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.imagen
