# coding=utf-8
# Modelos para la aplicación "Cursos".

# Standard Python/Django libraries
import datetime
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
# Third party libraries
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
# Local libraries
# None yet

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
    autor = models.ManyToManyField(User)
    nombre = models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    html = RichTextField(
        help_text="Descripción o instrucciones del recurso si es un adjunto o URL; contenido completo si es un texto o multimedia para deplegar en línea en la lección. Puede ser HTML."
        )
    tipo = models.CharField(
        max_length=5,
        choices=TIPOS_RECURSO
        )
    #Atributos opcionales
    adjunto = models.FileField(
        upload_to='recurso_adjunto',
        blank=True, help_text="Adjunto que se guardará con el recurso, como una imágen, PDF, video, etc."
        )
    url = models.URLField(
        blank=True,
        help_text="URL del recurso si proviene de otro sitio, como Youtube, Slideshare, etc."
        )
    #Metadatos opcionales
    nombre_corto=models.CharField(
        max_length=30,
        blank=True,
        help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. Máximo 30 caracteres."
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
        return "recursos/%s/%s/" % (self.tipo, self.id )

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
        User,
        help_text="Autor de esta lección."
        )
    nombre = models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    fecha_publicacion = models.DateField()
    fecha_actualizacion = models.DateField()
    recursos = models.ManyToManyField(
        Recurso,
        help_text="Recursos que se utilizan para apoyar este desempeño. Aparecen adjuntos al texto HTML.",
        blank=True
        )
    cuerpo = RichTextField(
        blank=True,
        help_text="Cuerpo de la lección que se deplegará para el estudiante."
        )
    #Metadatos opcionales
    tags = TaggableManager(help_text="Lista de tags separados por comas.")
    notas_profesor = RichTextField(
        blank=True,
        help_text="Notas para el profesor.")
    duracion = models.IntegerField(
        help_text="Tiempo requerido para lograr este desempeño en minutos.",
        verbose_name="Duración"
        )
    
    class Meta:
        ordering=['nombre']
        verbose_name="Desempeño de comprensión"
        verbose_name_plural="Desempeños de comprensión"
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "leccion/%s/" % self.id 


class Curso(models.Model):
    """
    Un curso está definido por un conjunto de tópicos generativos, metas de comprensión, desempeños de comprensión y recursos. Un proyecto es un tipo de curso.
    """
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
        max_length=16,
        unique=True,
        validators=[RegexValidator(regex='^[A-Z]{1,5}-\d{1,4}-?[a-z]??',
        message="No es un código de curso válido. Intente de nuevo. Los códigos válidos se ajustan a la expresión regular anterior.")],
        help_text="Código del curso. Debe ser único y de máximo 12 caracteres. Solo puede contener números, letras y guiones así: \^[A-Z]{1,5}-\\d{1,4}-?[a-z]??$"
        )
    nombre=models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
        )
    profesores = models.ManyToManyField(
        User,
        related_name='profesores',
        help_text="Autores y profesores del curso. Debe haber al menos uno."
        )
    acceso = models.CharField(
        max_length=5,
        choices=TIPOS_ACCESO,
        default = ABIERTO_LIBRE
        )
    cupos = models.IntegerField(
        blank=True,
        null=True,
        help_text="Cupo máximo del curso."
        )
    inscritos = models.ManyToManyField(
        User,
        related_name='inscritos',
        blank=True,
        help_text="Agregar alumnos a este curso."
        )
    
    #Atributos de diseño curricular (también obligatorios)
    hilos_conductores = models.ManyToManyField(
        HiloConductor,
        through='HilosConductoresCurso'
        )
    topicos_generativos = models.ManyToManyField(
        TopicoGenerativo,
        through='TopicosGenerativosCurso'
        )
    metas_de_comprension = models.ManyToManyField(
        MetaDeComprension,
        through='MetasDeComprensionCurso'
        )
    desempenos_de_comprension = models.ManyToManyField(
        DesempenoDeComprension,
        through='DesempenosCurso'
    )
    #Atributos opcionales
    imagen_destacada=models.ImageField(
        upload_to='curso_imagen_destacada',
        blank=True
        )
    #Metadatos
    tags = TaggableManager(help_text="Lista de tags separados por comas.")
    
    class Meta:
        verbose_name_plural="Cursos"
        ordering=['nombre']
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "cursos/%s/" % self.codigo

class HilosConductoresCurso(models.Model):
    """
    Contiene la relación entre Hilos conductores y cursos, junto a información adicional sobre la relación.
    """
    hilo_conductor=models.ForeignKey(HiloConductor)
    curso=models.ForeignKey(Curso)

class TopicosGenerativosCurso(models.Model):
    """
    Contiene la relación entre Tópicos generativos y cursos, junto a información adicional sobre la relación.
    """
    topico_generativo=models.ForeignKey(TopicoGenerativo)
    curso=models.ForeignKey(Curso)
    
class MetasDeComprensionCurso(models.Model):
    """
    Contiene la relación entre Metas de comprensión y cursos, junto a información adicional sobre la relación.
    """
    meta_de_comprension=models.ForeignKey(MetaDeComprension)
    curso=models.ForeignKey(Curso)

class DesempenosCurso(models.Model):
    """
    Contiene la relación entre Desempeños y cursos, junto a información adicional sobre el desempeño en ese curso.
    """
    desempeno=models.ForeignKey(DesempenoDeComprension)
    curso=models.ForeignKey(Curso)
    orden=models.IntegerField()

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