# coding=utf-8
# Modelos para la aplicación "Roubo-WLPE (Woodworking learning and publising environment)".
# VERSION 0.14

# Standard Python/Django libraries
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
# Third party libraries
# from ckeditor.fields import models.TextField
from taggit.managers import TaggableManager
# Local libraries
# None yet


# MODELOS PRINCIPALES
class Recurso(models.Model):
    """
    Representa una publicación genérica que puede verse como una entrada de blog, un tutorial,
    un proyecto, una biblioteca de recursos comentados, un libro, etc.
    """
    # Constantes
    BLOG = 'BLG'
    GALERIA = 'GLR'
    PROYECTO = 'PRY'
    TUTORIAL = 'TUT'
    VIDEO = 'VID'
    DOCUMENTO = 'DOC'  # puede ser pdf, epub, etc. Doc no es .doc, sino documento.
    TIPOS_RECURSO = (
        (BLOG, 'Blog'),
        (GALERIA, 'Galería'),
        (PROYECTO, 'Proyecto'),
        (TUTORIAL, 'Tutorial'),
        (VIDEO, 'Video'),
        (DOCUMENTO, 'Doc'),
    )
    # Atributos básicos y obligatorios
    autor = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='RecursosAutores'
    )
    nombre = models.CharField(
        max_length=150,
        help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
    )
    nombre_corto = models.SlugField(
        max_length=50,
        help_text="Nombre corto que se usa para la URL: letras, números, guiones, rayas). Debe ser único."
    )
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_actualizacion = models.DateField(default=datetime.date.today)
    cuerpo = models.TextField(
        help_text="Descripción o instrucciones del recurso si es un adjunto \
                  o URL; contenido completo si es un texto o multimedia para \
                  deplegar en línea en la lección. Puede ser HTML."
    )
    tipo = models.CharField(
        max_length=5,
        choices=TIPOS_RECURSO
    )
    # Atributos opcionales
    # adjunto = models.FileField(
    # upload_to='recurso_adjunto',
    # blank=True,
    # help_text="Adjunto que se guardará con el recurso, como una imágen, PDF, video, etc."
    # )
    url = models.URLField(
        blank=True,
        help_text="URL del recurso si proviene de otro sitio, como Youtube, Slideshare, o si también fue publicado en otro lugar."
    )
    # Metadatos opcionales
    imagen_destacada = models.ImageField(
        blank=True,
        upload_to='recursos',
        help_text='Imagen que se verá en los destacados y listas del recurso.'
    )
    tags = TaggableManager(help_text='Lista de tags separados por comas.', blank=True)

    class Meta:
        ordering = ['nombre_corto']
        verbose_name_plural = 'Recursos'

    class Admin:
        pass

    def __str__(self):
        return '{0} [{1}]'.format(self.nombre, self.tipo)

    def get_absolute_url(self):
        return reverse('recurso_detalle', kwargs={'tipo': self.tipo, 'nombre_corto': self.nombre_corto})


class Destacado(models.Model):
    """
    Recursos destacados para sliders, landings, etc.
    """
    recurso = models.ForeignKey(Recurso)
    sticky = models.BooleanField(default=False, blank=True)
    orden = models.IntegerField(default=1, blank=True)

    class Admin:
        pass

    class Meta:
        verbose_name_plural = 'Destacados'

    def __str__(self):
        return '{0} {1} {2} sticky: {3}'.format(self.orden, self.recurso.nombre_corto,
                                                self.recurso.tipo, self.sticky)


class Contacto(models.Model):
    """Comentario creado por un usuario.
    """
    # autor_registrado = models.ForeignKey(settings.AUTH_USER_MODEL)
    autor = models.CharField(max_length=50)
    email = models.EmailField()
    url = models.URLField(blank=True)
    fecha = models.DateField(default=datetime.date.today)
    texto = models.TextField()
    acepto_tratamiento = models.BooleanField(blank=False)
    acepto_contacto = models.BooleanField()

    class Meta:
        ordering = ['fecha']

    class Admin:
        verbose_name = 'Contacto del sitio.'

    def __str__(self):
        return 'Contacto {0}'.format(self.fecha)

    def get_absolute_url(self):
        # return reverse()
        return '/contacto/{0}'.format(self.pk)

# Atributos de los cursos.

# class HiloConductor(models.Model):
#     nombre=models.TextField(help_text="Las metas de comprensión de nivel superior que abarcan todo un proceso.")
#     nombre_corto=models.SlugField(
#         max_length=50,
#         blank=True,
#         help_text="Nombre corto que se usa para la URL: letras, números, guiones, rayas). Debe ser único."
#     )
#
#     class Meta:
#         ordering=['nombre']
#         verbose_name_plural='Hilos conductores'
#         verbose_name='Hilo conductor'
#
#     class Admin:
#         pass
#
#     def __str__(self):
#         return self.nombre_corto
#
#     def get_absolute_url(self):
#         return "hilos/%s/" % self.id
#
#
# class TopicoGenerativo(models.Model):
#     nombre=models.TextField(help_text="Un tópico generativo es una idea compleja, \
#              profunda, que se conecta con otras ideas o conceptos importantes de una \
#              disciplina. Guía el diseño de una unidad curricular. Es comparable con lo \
#              otros han llamado grandes ideas. P. ej. La relación entre las preopiedades \
#              físicas de la madera y los ensambles.")
#     nombre_corto=models.CharField(
#         max_length=30,
#         blank=True,
#         help_text="Nombre corto que se verá en listas y otros lugares. Debe ser legible. \
#                   Máximo 30 caracteres. Use ortografía de título."
#     )
#
#     class Meta:
#         ordering=['nombre']
#         verbose_name="Tópico generativo"
#         verbose_name_plural="Tópicos generativos"
#
#     class Admin:
#         pass
#
#     def __str__(self):
#         if self.nombre_corto:
#             return self.nombre_corto
#         return self.nombre
#
#     def get_absolute_url(self):
#         return "topicos/%s/" % self.id
#
#
# class MetaCom(models.Model):
#     nombre=models.TextField(help_text="Una meta de comprensión identifica lo que se \
#             busca que lo estudiantes logren saber y saber hacer. Puede ser un enunciado \
#             o una pregunta. P. Ej. Los estudiantes comprenderán cómo utilizar la sierra sinfín \
#             de manera segura; o ¿Cómo operar la sierra sinfín de manera segura?")
#     nombre_corto=models.SlugField(
#         max_length=50,
#         blank=True,
#         help_text="Nombre corto que se usa para la URL: letras, números, guiones, rayas). \
#                   Debe ser único."
#         )
#
#     class Meta:
#         ordering=['nombre']
#         verbose_name="Meta de comprensión"
#         verbose_name_plural="Metas de comprensión"
#
#     class Admin:
#         pass
#
#     def __str__(self):
#         if self.nombre_corto:
#             return self.nombre_corto
#         return self.nombre
#
#     def get_absolute_url(self):
#         return "metas/%s/" % self.id
#
#
# class Criterio(models.Model):
#     """Criterio de evaluación. Se relaciona directamente con una o más metas.
#     """
#     nombre = models.CharField(
#         max_length=550,
#         help_text="Nombre del criterio de evaluación. P. ej. Corte a escuadra, Ajuste del ensamble o suavidad de las superficie."
#         )
#     nombre_corto=models.SlugField(
#         max_length=50,
#         help_text="Nombre corto que se usa para la URL: letras, números, guiones, rayas). Debe ser único."
#         )
#     descripcion = models.TextField(
#         help_text="Descripción o notas sobre el criterio.",
#         blank = True
#         )
#     metas = models.ManyToManyField(
#         MetaCom,
#         through='CriteriosMetas',
#         help_text="Metas relaciodas con este desempeño.",
#         )
#
#
# class Desempeno(models.Model):
#     """
#     Un desempeño es la unidad de contenido de un curso o proyecto. Puede ser una clase, \
#     una parte de una clase o tomar más de una sesión. Una secuencia de desempeños progresivamente \
#     más complejos representa la secuencia básica de un curso. Cada desempeño que busca avanzar \
#     hacia el logro de una o más metas de comprensión. Puede ser parte de una secuencia para \
#     conformar un curso o proyecto o ser independiente.
#     """
#     #Atributos básicos y obligatorios
#     autor = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#         through='DesempenosAutores',
#         help_text="Autor de esta lección."
#         )
#     nombre = models.CharField(
#         max_length=150,
#         help_text="Ojo con la ortografía de los títulos en español. Máximo 150 caracteres."
#         )
#     nombre_corto=models.SlugField(
#         max_length=50,
#         help_text="Nombre corto que se usa para la URL: letras, números, guiones, rayas). Debe ser único."
#         )
#     fecha_creacion = models.DateField()
#     fecha_actualizacion = models.DateField()
#     recursos = models.ManyToManyField(
#         Recurso,
#         through = 'DesempenosRecursos',
#         help_text="Recursos que se utilizan para apoyar este desempeño. Aparecen adjuntos al texto HTML.",
#         blank=True
#         )
#     cuerpo = models.TextField(
#         blank=True,
#         help_text="Cuerpo de la lección que se deplegará para el estudiante."
#         )
#     #Metadatos opcionales
#     #destacado=models.BooleanField(default=False, help_text="Los recursos marcados \
#       como destacados son titulares en los listados y landings de secciones.")
#     imagen_destacada=models.ImageField(
#         blank=True,
#         upload_to="recurso_adjunto",
#         help_text="Imagen que se verá en los destacados y listas del recurso."
#         )
#     notas_profesor = models.TextField(
#         blank=True,
#         help_text="Notas para el profesor.")
#     duracion = models.IntegerField(
#         help_text="Tiempo aproximado requerido para lograr este desempeño en minutos.",
#         verbose_name="Duración"
#         )
#     tags = TaggableManager(help_text="Lista de tags separados por comas.")
#
#     class Meta:
#         ordering=['nombre']
#         verbose_name="Desempeño de comprensión"
#         verbose_name_plural="Desempeños de comprensión"
#
#     class Admin:
#         pass
#
#     def __str__(self):
#         return self.nombre
#
#     def get_absolute_url(self):
#         return reverse('desempeno_detalle', kwargs={'nombre_corto': self.nombre_corto})
#
#
# class Curso(models.Model):
#     """Un curso está definido por un conjunto de tópicos generativos, metas de comprensión, \
#       desempeños de comprensión (y recursos relacionados con ellos). Un proyecto es un tipo de \
#       curso."""
#     #Constantes
#     ABIERTO_LIBRE = 'AB-L'
#     ABIERTO_CON_INSCRIPCION = 'AB-I'
#     PRIVADO = 'PR'
#     VIP = 'VIP'
#     TIPOS_ACCESO = (
#         (ABIERTO_LIBRE,"Abierto y libre"),
#         (ABIERTO_CON_INSCRIPCION,"Abierto con inscripción"),
#         (PRIVADO,"Exclusivo para miembros"),
#         (VIP,"Requiere autorización especial")
#     )
#     #Atributos básicos y obligatorios
#     codigo = models.CharField(
#         max_length = 12,
#         validators = [RegexValidator(regex='^(?P<codigo_tipo>[A-Z])(?P<codigo_tema>[A-Z]{3,5})-(?P<nivel>[0-9]{,3})-(?P<version>[0-9a-z]{,4}$)',
#         message = "No es un código de curso válido. Intente de nuevo. Los códigos válidos se ajustan a la expresión regular anterior.")],
#         help_text = "Código del curso. Se valida con la siguiente expresión regular: ^(?P<codigo_tipo>[A-Z])(?P<codigo_tema>[A-Z]{3,5})-(?P<nivel>[0-9]{,3})(?P<version>[0-9a-z]{,4}$)",
#         verbose_name = "Código",
#         )
#     nombre=models.CharField(
#         max_length = 150,
#         help_text = "Ojo con la ortografía de los títulos en español. Máximo 150 caracteres.",
#         blank = True
#         )
#     fecha_inicio=models.DateField(help_text="La fecha de inicio es obligatoria, aunque el curso no tenga fecha de finalización.")
#     profesores = models.ManyToManyField(
#         settings.AUTH_USER_MODEL,
#         through = 'CursosProfesores',
#         related_name='profesores',
#         help_text="Autores y profesores del curso. Debe haber al menos uno."
#         )
#     acceso = models.CharField(
#         max_length=5,
#         choices=TIPOS_ACCESO,
#         default = ABIERTO_LIBRE
#         )
#
#     #Atributos de diseño curricular (también obligatorios)
#     hilos_conductores = models.ManyToManyField(
#         HiloConductor,
#         through='CursosHilosConductores'
#     )
#     topicos_generativos = models.ManyToManyField(
#         TopicoGenerativo,
#         through='CursosTopicosGenerativos'
#         )
#     metas = models.ManyToManyField(
#         MetaCom,
#         through='CursosMetas'
#         )
#     desempenos = models.ManyToManyField(
#         Desempeno,
#         through='CursosDesempenos'
#     )
#     #Atributos del curso que requiere inscripción
#     cupos = models.IntegerField(
#         blank=True,
#         help_text="Cupo máximo del curso.",
#         )
#     #Metadatos
#     #destacado=models.BooleanField(default=False, help_text="Los recursos marcados como destacados son titulares en los listados y landings de secciones.")
#     imagen_destacada=models.ImageField(
#         upload_to='cursos',
#         blank=True
#         )
#     tags = TaggableManager(
#         blank=True,
#         help_text="Lista de tags separados por comas."
#         )
#
#     class Meta:
#         verbose_name_plural="Cursos"
#         verbose_name='Curso'
#         ordering=['nombre']
#
#     class Admin:
#         pass
#
#     def __str__(self):
#         return self.codigo, self.nombre
#
#     def get_absolute_url(self):
#         #return "cursos/%s/" % self.codigo
#         return reverse('curso_inicio', kwargs={'codigo': self.codigo})
#
#
# # MODELOS PARA LAS RELACIONES THROUGH= DE LOS CAMPOS M2M.


class RecursosAutores(models.Model):
    """recurso=Recurso, autor=User
    Contiene la relación entre autores y recursos.
    """
    recurso = models.ForeignKey(Recurso, verbose_name="Recurso")
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Autor")

    class Meta:
        verbose_name_plural = "Autores y recursos"
        verbose_name = "Autores y recursos"

    def __str__(self):
        return "Autor o recurso (relación)"
#
#
# class CriteriosMetas:
#     """Contiene la relación entre criterios y metas y el orden para cada relación.
#     """
#     criterio = models.ForeignKey(Criterio, verbose_name="Criterios")
#     meta = models.ForeignKey(MetaCom, verbose_name="Metas")
#     orden = models.IntegerField()
#
#     class Meta:
#         verbose_name = "Criterios y metas"
#         verbose_name_plural = "Criterios y metas"
#
#     def __str__(self):
#         return "Criterio meta (relación)"
#
#
# class DesempenosAutores(models.Model):
#     """desempeno=Desempeno, autor=User
#     Contiene la relación entre desempeños de comprensión y autores
#     """
#     desempeno=models.ForeignKey(Desempeno, verbose_name="Desempeños de comprensión")
#     autor = models.ForeignKey(settings.AUTH_USER_MODEL)
#
#     class Meta:
#         verbose_name="Autores y desempeños de comprensión"
#         verbose_name_plural="Autores y desempeños de comprensión"
#
#     def __str__(self):
#         return "Autor o desempeño (relación)"
#
#
# class DesempenosMetas(models.Model):
#     """desempeno=Desempeno, autor=User
#     Contiene la relación entre desempeños de comprensión y autores
#     """
#     desempeno=models.ForeignKey(Desempeno, verbose_name="Desempeños de comprensión")
#     meta = models.ForeignKey(MetaCom)
#
#     class Meta:
#         verbose_name="Autores y desempeños de comprensión"
#         verbose_name_plural="Autores y desempeños de comprensión"
#
#     # def __str__(self):
#     #     return "Autor o desempeño (relación)"
#
#
# class DesempenosRecursos(models.Model):
#     """desempeno=Desempeno, recurso=Recurso
#     Contiene la relación entre desempeños de comprensión y recursos
#     """
#     desempeno=models.ForeignKey(Desempeno, verbose_name="Desempeño de comprensión")
#     recurso=models.ForeignKey(Recurso, verbose_name="Recurso")
#
#     class Meta:
#         verbose_name_plural="Desempeños de comprensión y recursos"
#         verbose_name="Desempeños de comprensión y recursos"
#
#     def __str__(self):
#         return "Recurso y desempeño (relación)"
#
#
#
# class CursosProfesores(models.Model):
#     """curso=Curso, profesor=User
#     Contiene la relación entre cursos y profesores.
#     """
#     curso=models.ForeignKey(Curso)
#     profesor=models.ForeignKey(settings.AUTH_USER_MODEL)
#
#     class Meta:
#         verbose_name="Cursos y profesores"
#         verbose_name_plural="Cursos y profesores"
#
#     def __str__(self):
#         return "Curso y profesor (relación)"
#
#
# class CursosHilosConductores(models.Model):
#     """hilo_conductor=HiloConductor, curso=Curso
#     Contiene la relación entre Hilos conductores y cursos, junto a información adicional sobre la relación.
#     """
#     hilo_conductor=models.ForeignKey(HiloConductor)
#     curso=models.ForeignKey(Curso)
#
#     class Meta:
#         verbose_name="Hilos conductores y cursos"
#         verbose_name_plural="Hilos conductores y cursos"
#
#     def __str__(self):
#         return "Curso e hilo conductor (relación)"
#
#
# class CursosTopicosGenerativos(models.Model):
#     """topico_generativo=TopicoGenerativo, curso=Curso
#     Contiene la relación entre Tópicos generativos y cursos, junto a información adicional sobre la relación.
#     """
#     topico_generativo=models.ForeignKey(TopicoGenerativo, verbose_name="Tópico generativo")
#     curso=models.ForeignKey(Curso)
#
#     class Meta:
#         verbose_name="Cursos y tópicos generativos"
#         verbose_name_plural="Cursos y tópicos generativos"
#
#     def __str__(self):
#         return "Curso y tópico generativo (relación)"
#
#
# class CursosMetas(models.Model):
#     """meta_de_comprension=Meta, curso=Curso
#     Contiene la relación entre Metas de comprensión y cursos, junto a información adicional sobre la relación.
#     """
#     meta=models.ForeignKey(MetaCom, verbose_name="Meta de comprensión")
#     curso=models.ForeignKey(Curso)
#
#     class Meta:
#         verbose_name="Cursos y metas de comprensión"
#         verbose_name_plural="Cursos y metas de comprensión"
#
#     def __str__(self):
#         return "Cursos y metas de comprensión (relación)"
#
#
# class CursosDesempenos(models.Model):
#     """desempeno=Desempeno, curso=Curso, orden=int
#     Contiene la relación entre Desempeños y cursos, junto a información adicional sobre el desempeño en ese curso.
#     """
#     desempeno=models.ForeignKey(Desempeno, verbose_name="Desempeño")
#     curso=models.ForeignKey(Curso)
#     orden=models.IntegerField()
#
#     class Meta:
#         verbose_name="Cursos y metas de comprensión"
#         verbose_name_plural="Desempeños de comprension y cursos"
#
#     def __str__(self):
#         return "Curso y desempeño (relación)"
