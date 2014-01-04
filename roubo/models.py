# coding=utf-8
# Modelos para la aplicación "Roubo".
# VERSION 0.12

# Standard Python/Django libraries
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
# Third party libraries
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Local libraries
# None yet

#MODELOS PRINCIPALES
class Recurso(models.Model):
    """
    Representa cualquier tipo de recurso de aprendizaje que se puede utilizar como apoyo a un desempeño o ser independiente, como una entrada de blog-tutorial o una biblioteca de recursos comentados.
    """
    #Constantes
    VIDEO='VID'
    AUDIO='AUD'
    IMAGEN='IMG'
    TEXTO='TEX'
    MULTIMEDIA='MLT'
    TIPOS_RECURSO = (
        (VIDEO, 'Video'),
        (AUDIO, 'Audio'),
        (IMAGEN, 'Imagen'),
        (TEXTO, 'Texto'),
        (MULTIMEDIA, 'Multimedia'),
    )
    #Atributos básicos y obligatorios
    autor = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='RecursosAutores'
        )
    nombre = models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    nombre_corto=models.SlugField(
        max_length=50,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres (letras, números, guiones, rayas). Debe ser único. Se usa para crear la URL del recurso y buscarlo en la bd."
        )
    cuerpo = RichTextField(
        help_text="Descripción o instrucciones del recurso si es un adjunto o URL; contenido completo si es un texto o multimedia para deplegar en línea en la lección. Puede ser HTML."
        )
    tipo = models.CharField(
        max_length=5,
        choices=TIPOS_RECURSO
        )
    #Atributos opcionales
    adjunto = models.FileField(
        upload_to='recurso_adjunto',
        blank=True,
        help_text="Adjunto que se guardará con el recurso, como una imágen, PDF, video, etc."
        )
    url = models.URLField(
        blank=True,
        help_text="URL del recurso si proviene de otro sitio, como Youtube, Slideshare, etc."
        )
    #Metadatos opcionales
    destacado=models.BooleanField(default=False, help_text="Los recursos marcados como destacados son titulares en los listados y landings de secciones.")
    imagen_destacada=models.ImageField(
        blank=True,
        upload_to="recurso_adjunto",
        help_text="Imagen que se verá en los destacados y listas del recurso."
        )
    tags = TaggableManager(help_text="Lista de tags separados por comas.")
    
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
        return reverse('recurso_detalle', kwargs={'tipo': self.tipo, 'nombre_corto': self.nombre_corto})

#Atributos pedagógicos de los cursos. Inspirado ligeramente en Collaborative Curriculum Design Tool ofrecido por Wide World en https://learnweb.harvard.edu/ccdt/index.cfm y las ideas sobre diseño curricular, EpC/TFU, de los investigadores de Proyecto Cero en la Escuela Posgragos en Educación de la Universidad de Harvard.

class HiloConductor(models.Model):
    nombre=RichTextField(help_text="Las metas de comprensión de nivel superior que abarcan todo el proceso.")
    nombre_corto=models.CharField(
        max_length=30,
        blank=True,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres. Use ortografía de título."
    )
    
    class Meta:
        ordering=['nombre']
        verbose_name_plural='Hilos conductores'
        verbose_name='Hilo conductor'
    
    class Admin:
        pass
    
    def __unicode__(self):
        if self.nombre_corto:
            return self.nombre_corto
        return self.nombre
    
    def get_absolute_url(self):
        return "hilos/%s/" % self.id
        

class TopicoGenerativo(models.Model):
    nombre=RichTextField(help_text="Un tópico generativo es una idea compleja, profunda, que se conecta con otras ideas o conceptos importantes de la disciplina. Guía el diseño de una unidad curricular, como un curso.")
    nombre_corto=models.CharField(
        max_length=30,
        blank=True,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres. Use ortografía de título."
    )
        
    class Meta:
        ordering=['nombre']
        verbose_name="Tópico generativo"
        verbose_name_plural="Tópicos generativos"
    
    class Admin:
        pass
    
    def __unicode__(self):
        if self.nombre_corto:
            return self.nombre_corto
        return self.nombre
    
    def get_absolute_url(self):
        return "topicos/%s/" % self.id    

class MetaDeComprension(models.Model):
    nombre=RichTextField(help_text="Una meta de comprensión identifica lo que se busca que lo estudiantes logren saber y saber hacer. Puede ser un enunciado o una pregunta. P. Ej. Los estudiantes comprenderán cómo utilizar la sierra sinfín de manera segura; o ¿Cómo operar la sierra sinfín de manera segura?")
    nombre_corto=models.CharField(
        max_length=30,
        blank=True,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres. Use ortografía de título."
        )
        
    class Meta:
        ordering=['nombre']
        verbose_name="Meta de comprensión"
        verbose_name_plural="Metas de comprensión"
    
    class Admin:
        pass
    
    def __unicode__(self):
        if self.nombre_corto:
            return self.nombre_corto
        return self.nombre
    
    def get_absolute_url(self):
        return "metas/%s/" % self.id 

class DesempenoDeComprension(models.Model):
    """
    Un desempeño es la unidad de contenido de un curso o proyecto. Una secuencia de desempeños progresivamente más complejos representa la secuencia básica de un curso. Cada desempeño que busca avanzar hacia el logro de una o más metas de comprensión. Puede ser parte de una secuencia para conformar un curso o proyecto o ser independiente.
    """
    #Atributos básicos y obligatorios
    autor = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='DesempenosDeComprensionAutores',
        help_text="Autor de esta lección."
        )
    nombre = models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    nombre_corto=models.SlugField(
        max_length=50,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres (letras, números, guiones, rayas). Debe ser único. Se usa para crear la URL del recurso y buscarlo en la bd."
        )
    fecha_publicacion = models.DateField()
    fecha_actualizacion = models.DateField()
    recursos = models.ManyToManyField(
        Recurso,
        through = 'DesempenosDeComprensionRecursos',
        help_text="Recursos que se utilizan para apoyar este desempeño. Aparecen adjuntos al texto HTML.",
        blank=True
        )
    cuerpo = RichTextField(
        blank=True,
        help_text="Cuerpo de la lección que se deplegará para el estudiante."
        )
    #Metadatos opcionales
    destacado=models.BooleanField(default=False, help_text="Los recursos marcados como destacados son titulares en los listados y landings de secciones.")
    imagen_destacada=models.ImageField(
        blank=True,
        upload_to="recurso_adjunto",
        help_text="Imagen que se verá en los destacados y listas del recurso."
        )
    notas_profesor = RichTextField(
        blank=True,
        help_text="Notas para el profesor.")
    duracion = models.IntegerField(
        help_text="Tiempo requerido para lograr este desempeño en minutos.",
        verbose_name="Duración"
        )
    tags = TaggableManager(help_text="Lista de tags separados por comas.")
    
    class Meta:
        ordering=['nombre']
        verbose_name="Desempeño de comprensión"
        verbose_name_plural="Desempeños de comprensión"
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('desempeno_detalle', kwargs={'nombre_corto': self.nombre_corto})


class Curso(models.Model):
    """Un curso está definido por un conjunto de tópicos generativos, metas de comprensión, desempeños de comprensión (y recursos y relacionados con ellos). Un proyecto es un tipo de curso."""
    #Constantes
    ABIERTO_LIBRE = 'AB-L'
    ABIERTO_CON_INSCRIPCION = 'AB-I'
    PRIVADO = 'PR'
    VIP = 'VIP'
    TIPOS_ACCESO = (
        (ABIERTO_LIBRE,"Abierto y libre"),
        (ABIERTO_CON_INSCRIPCION,"Abierto con inscripción"),
        (PRIVADO,"Exclusivo para miembros"),
        (VIP,"Requiere autorización especial")
    )
    #Atributos básicos y obligatorios
    codigo=models.CharField(
        max_length=12,
        validators=[RegexValidator(regex='^(?P<codigo_tipo>[A-Z])(?P<codigo_tema>[A-Z]{3,5})-(?P<nivel>[0-9]{,3})(?P<version>[a-z]{,3}$)',
        message="No es un código de curso válido. Intente de nuevo. Los códigos válidos se ajustan a la expresión regular anterior.")],
        help_text="Código del curso. Se valida con la siguiente expresión regular: ^(?P<codigo_tipo>[A-Z])(?P<codigo_tema>[A-Z]{3,5})-(?P<nivel>[0-9]{,3})(?P<version>[a-z]{,3}$)",
        verbose_name="Código",
        )
    nombre=models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    fecha_inicio=models.DateField(help_text="La fecha de inicio es obligatoria, aunque el curso no tenga fecha de finalización.")
    profesores = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through = 'CursosProfesores',
        related_name='profesores',
        help_text="Autores y profesores del curso. Debe haber al menos uno."
        )
    acceso = models.CharField(
        max_length=5,
        choices=TIPOS_ACCESO,
        default = ABIERTO_LIBRE
        )
    
    #Atributos de diseño curricular (también obligatorios)
    hilos_conductores = models.ManyToManyField(
        HiloConductor,
        through='CursosHilosConductores'
        )
    topicos_generativos = models.ManyToManyField(
        TopicoGenerativo,
        through='CursosTopicosGenerativos'
        )
    metas_de_comprension = models.ManyToManyField(
        MetaDeComprension,
        through='CursosMetasDeComprension'
        )
    desempenos_de_comprension = models.ManyToManyField(
        DesempenoDeComprension,
        through='CursosDesempenosDeComprension'
    )
    #Atributos del curso que requiere inscripción
    cupos = models.IntegerField(
        blank=True,
        null=True,
        help_text="Cupo máximo del curso."
        )
    #Metadatos
    destacado=models.BooleanField(default=False, help_text="Los recursos marcados como destacados son titulares en los listados y landings de secciones.")
    imagen_destacada=models.ImageField(
        upload_to='curso_imagen_destacada',
        blank=True
        )
    tags = TaggableManager(
        blank=True,
        help_text="Lista de tags separados por comas."
        )
    
    class Meta:
        verbose_name_plural="Cursos"
        verbose_name='Curso'
        ordering=['nombre']
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        #return "cursos/%s/" % self.codigo
        return reverse('curso_inicio', kwargs={'codigo': self.codigo})
 
   


# MODELOS PARA LAS RELACIONES THROUGH= DE LOS CAMPOS M2M.
class RecursosAutores(models.Model):
    """recurso=Recurso, autor=User
    Contiene la relación entre autores y recursos.
    """
    recurso=models.ForeignKey(Recurso, verbose_name="Recurso")
    autor=models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Autor")
    
    class Meta:
        verbose_name_plural="Relación autores y recursos"
        verbose_name="Relaciones autores y recursos"
        
    def __unicode__(self):
        return "Autor o recurso (relación)"


class DesempenosDeComprensionAutores(models.Model):
    """desempeno_de_comprension=DesempenoDeComprension, autor=User
    Contiene la relación entre desempeños de comprensión y autores
    """
    desempeno_de_comprension=models.ForeignKey(DesempenoDeComprension, verbose_name="Desempeños de comprensión")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        verbose_name="Relación autores y desempeños de comprensión"
        verbose_name_plural="Relaciones autores y desempeños de comprensión"
    
    def __unicode__(self):
        return "Autor o desempeño (relación)"
    

class DesempenosDeComprensionRecursos(models.Model):
    """desempeno_de_comprension=DesempenoDeComprension, recurso=Recurso
    Contiene la relación entre desempeños de comprensión y recursos
    """
    desempeno_de_comprension=models.ForeignKey(DesempenoDeComprension, verbose_name="Desempeño de comprensión")
    recurso=models.ForeignKey(Recurso, verbose_name="Recurso")
    
    class Meta:
        verbose_name_plural="Relación desempeños de comprensión y recursos"
        verbose_name="Relaciones desempeños de comprensión y recursos"
    
    def __unicode__(self):
        return "Recurso y desempeño (relación)"
        
    
class CursosProfesores(models.Model):
    """curso=Curso, profesor=User
    Contiene la relación entre cursos y profesores.
    """
    curso=models.ForeignKey(Curso)
    profesor=models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        verbose_name="Relación cursos y profesores"
        verbose_name_plural="Relaciones cursos y profesores"

    def __unicode__(self):
            return "Curso y profesor (relación)"


class CursosHilosConductores(models.Model):
    """hilo_conductor=HiloConductor, curso=Curso
    Contiene la relación entre Hilos conductores y cursos, junto a información adicional sobre la relación.
    """
    hilo_conductor=models.ForeignKey(HiloConductor)
    curso=models.ForeignKey(Curso)
    
    class Meta:
        verbose_name="Relación hilos conductores y cursos"
        verbose_name_plural="Relaciones hilos conductores y cursos"
    
    def __unicode__(self):
        return "Curso e hilo conductor (relación)"


class CursosTopicosGenerativos(models.Model):
    """topico_generativo=TopicoGenerativo, curso=Curso
    Contiene la relación entre Tópicos generativos y cursos, junto a información adicional sobre la relación.
    """
    topico_generativo=models.ForeignKey(TopicoGenerativo, verbose_name="Tópico generativo")
    curso=models.ForeignKey(Curso)
    
    class Meta:
        verbose_name="Relación cursos y tópicos generativos"
        verbose_name_plural="Relaciones cursos y tópicos generativos"
        
    def __unicode__(self):
        return "Curso y tópico generativo (relación)"
    
    
class CursosMetasDeComprension(models.Model):
    """meta_de_comprension=MetaDeComprension, curso=Curso
    Contiene la relación entre Metas de comprensión y cursos, junto a información adicional sobre la relación.
    """
    meta_de_comprension=models.ForeignKey(MetaDeComprension, verbose_name="Meta de comprensión")
    curso=models.ForeignKey(Curso)

    class Meta:
        verbose_name="Relación cursos y metas de comprensión"
        verbose_name_plural="Relaciones cursos y metas de comprensión"

    def __unicode__(self):
        return "Cursos y metas de comprensión (relación)"


class CursosDesempenosDeComprension(models.Model):
    """desempeno=DesempenoDeComprension, curso=Curso, orden=int
    Contiene la relación entre Desempeños y cursos, junto a información adicional sobre el desempeño en ese curso.
    """
    desempeno_de_comprension=models.ForeignKey(DesempenoDeComprension, verbose_name="Desempeño de comprensión")
    curso=models.ForeignKey(Curso)
    orden=models.IntegerField()
    
    class Meta:
        verbose_name="Relación cursos y metas de comprensión"
        verbose_name_plural="Relaciones desempeños de comprension y cursos"
    
    def __unicode__(self):
            return "Curso y desempeño (relación)"

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