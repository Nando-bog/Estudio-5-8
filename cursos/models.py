# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class Curso(models.Model):
    """Un curso es una colección de contenidos ordenados de manera que permiten apoyar el desarrollo de competencias, habilidades o conocimientos. Un proyecto es un tipo de curso enfocado en la práctica mediante la creación de un artefacto.
    """
    nombre=models.CharField(max_length=150)
    
class Recurso(models.Model):
    """Un recurso es la unidad mínima de contenido de una lección. Es una secuencia de código HTML y puede contener un archivo adjunto.
    """
    titulo = models.CharField(max_length=150)
    url = models.URLField(blank=True)
    adjunto = models.FileField(upload_to='resources')
    tags = TaggableManager()

class Leccion(models.Model):
    """Una lección es la unidad mínima de contenido de un curso. Representa una sección de una clase o curso que tiene unidad temática. Puede ser parte de una secuencia para conformar un curso o proyecto o ser independiente. Contiene recursos organizados, detallados, relacionados, etc.
    """
    curso = models.ManyToManyField(Curso)
    titulo = models.CharField(max_length=150)
    autor = models.ManyToManyField(User)
    fecha_publicacion = models.DateField()
    fecha_actualizacion = models.DateField(auto_now=True)
    recursos = models.ManyToManyField(Recurso)
    tags = TaggableManager()
    