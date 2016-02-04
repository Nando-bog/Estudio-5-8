# coding=utf-8
# Version 0.1
# Maloof es el app para la adminstración de usuarios y perfiles en Estudio 5-8. Nombre inspirado en el ebanista californiano y el culto a la personalidad del artesano que representa su nombre.

from datetime import datetime
from uuid import uuid4
import csv
import os
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone


# Change the name of a user profile image on upload
def change_profile_filename(instance, filename):
    upload_to = "avatares"
    extension = filename.split('.')[-1]
    if instance.usuario.username:
        nombre_archivo = '{0}.{1}'.format(instance.usuario.username, extension)
    else:
        filename = '{0}.{1}'.format(uuid4().hex, extension)
    return os.path.join(upload_to, filename)


class Perfil(models.Model):
    """Datos que representan a una persona, un usuario de Estudio 5-8. Se relaciona con el modelo estándar de usuario de Django.
    """

    # CONSTANTES GÉNERO
    MAS = 'MAS'
    FEM = 'FEM'
    SEXOS = (
        (MAS, 'Masculino'),
        (FEM, 'Femenino'),
    )

    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    nick = models.CharField(max_length=20, help_text='¿Cómo quiere que lo llamemos?')
    fecha_nacimiento = models.DateField(blank=True, default=timezone.now())
    sexo = models.CharField(blank=True, max_length=3, choices=SEXOS)
    telefono = models.CharField(blank=True, max_length=15)
    pais = models.CharField(blank=True, max_length=100, choices=settings.PAISES)
    ciudad = models.CharField(blank=True, max_length=100)
    avatar = models.ImageField(blank=True, upload_to=change_profile_filename)
    intereses = models.TextField(blank=True)
    url = models.URLField(blank=True)
    ocupacion = models.CharField(blank=True, max_length=200)
    biografia = models.TextField(blank=True)
    tratamiento_datos = models.BooleanField(blank=False, default=False, help_text='Acepta la política de tratamiento de datos.')
    suscripcion = models.BooleanField(blank=False, default=False, help_text='¿Quiere recibir noticias de Estudio 5-8?')
    compartir_datos = models.BooleanField(blank=False, default=False, help_text='¿Acepta compartir sus datos de contacto con otros miembros de 5-8?')

    class Meta:
        ordering = ['nick']
        verbose_name_plural = 'Perfiles'

    class Admin:
        pass

    def __str__(self):
        return '{0} (perfil)'.format(self.usuario.username)
    