# coding=utf-8
# Modelos para la aplicación de Cursos

# Standard Python/Django library imports
import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
# Third party library imports
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Local library imports

#class Categoria(models.Model):
#    nombre = models.CharField(max_length=150, help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres.")
#    slug = models.SlugField(unique=True, help_text="Se usará para generar URLs. Admite letras, números y guiones. Debe ser único y máximo de 50 caracteres.")
#    descripcion = models.TextField(blank=True, help_text="Descripción de la categoría.")
#    
#    class Meta:
#        verbose_name_plural="Categorías"
#        ordering = ['nombre']
#    
#    class Admin:
#        pass
#    
#    def __unicode__(self):
#        return self.nombre
#    
#    def get_absolute_url(self):
#        return "cat/%s/" % self.slug  

class Curso(models.Model):
    """
    Un curso es una colección de contenidos ordenados con un criterio didáctico. Un proyecto es un tipo de curso enfocado en la práctica mediante la creación de un artefacto.
    """
    TIPOS_ACCESO = (
        ('AB-L',"Abierto y libre"),
        ('AB-I',"Abierto con inscripción"),
        ('CE',"Cerrado"),
    )
    #Atributos básicos y obligatorios
    codigo=models.CharField(max_length=16, unique=True, validators=[RegexValidator(regex='^[A-Z]{1,5}-\d{1,4}-?[a-z]??', message="No es un código de curso válido. Intente de nuevo. Los códigos válidos se ajustan a la expresión regular anterior.")], help_text="Código del curso. Debe ser único y de máximo 12 caracteres. Solo puede contener números, letras y guiones así: \^[A-Z]{1,5}-\\d{1,4}-?[a-z]??$")
    nombre=models.CharField(max_length=150, help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres.")
    profesor = models.ManyToManyField(User, help_text="Autores y profesores del curso. Debe haber al menos uno.")
    acceso = models.CharField(max_length=5, choices=TIPOS_ACCESO)
    #Atributos opcionales
    imagen_destacada=models.ImageField(upload_to='curso_imagen_destacada', blank=True)
    #Meta datos
    tags = TaggableManager(help_text="Lista de tagas separados por comas.")
    
    class Meta:
        verbose_name_plural="Cursos"
        ordering=['nombre']
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "cursos/%s/" % self.codigo 


class Recurso(models.Model):
    """
    Un recurso es la unidad mínima de contenido de una lección. Es una secuencia de código HTML y puede contener un archivo adjunto.
    """
    TIPOS_RECURSO = (
        ('VID', 'Video'),
        ('AUD', 'Audio'),
        ('IMG', 'Imagen'),
        ('TEX', 'Texto'),
        ('MULTI', 'Multimedia'),
    )
    #Atributos básicos y obligatorios
    autor = models.ManyToManyField(User)
    nombre = models.CharField(max_length=150, help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres.")
    html = RichTextField(help_text="Contenido de la lección en HTML. Este es el texto que el usuario podrá ver y el profesor agregar automáticamente a su lección.")
    tipo = models.CharField(max_length=5, choices=TIPOS_RECURSO)
    #Atributos opcionales
    adjunto = models.FileField(upload_to='resources', blank=True, help_text="Adjunto que se guardará con el recurso, como una imágen, PDF, video, etc.")
    url = models.URLField(blank=True, help_text="URL del recurso si proviene de otro sitio, como Youtube, Slideshare, etc.")
    #Meta datos opcionales
    nombre_corto=models.CharField(max_length=30, blank=True, help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres.")
    tags = TaggableManager()
    
    class Meta:
        ordering=['nombre']
        verbose_name_plural='Recursos'
        
    class Admin:
        pass
    
    def __unicode__(self):
        if self.nombre_corto:
            return self.nombre_corto
        return self.nombre
    
    def get_absolute_url(self):
        return "recursos/%s/" % self.id


class Leccion(models.Model):
    """Una lección es la unidad de contenido de un curso. Representa una sección de una clase o curso que tiene unidad temática. Puede ser parte de una secuencia para conformar un curso o proyecto o ser independiente. Contiene recursos organizados, detallados, relacionados, etc.
    """
    cursos = models.ManyToManyField(Curso)
    titulo = models.CharField(max_length=150)
    autor = models.ManyToManyField(User)
    fecha_publicacion = models.DateField()
    fecha_actualizacion = models.DateField(auto_now=True)
    recursos = models.ManyToManyField(Recurso)
    html = models.TextField(blank=True)
    tags = TaggableManager()