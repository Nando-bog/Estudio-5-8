#coding=utf-8
# Modelos para la aplicación "Studley", una caja de herramientas.
# La caja de herramientas personal de un usuario es una colección. Diseñar métodos para comparar, compartir, etc., colecciones. ¡Sigue siendo Studley!
# Version 0.11
from django.db import models
from django.conf import settings

class ClaseHerramienta(models.Model):
    """Clase de harramienta según su función: Alisado, Atornillado, Corte, Labrado, Perforación, Sujeción, Afilado, Golpeo, Seguridad, Marcación, Medición, Aseo
    """
    CLASES_HERRAMIENTAS = (
        (1, 'Afilado'),
        (1, 'Alisado'),
        (2, 'Atornillado'),
        (3, 'Aseo'),
        (4, 'Corte'),
        (5, 'Labrado'),
        (6, "Perforación"),
        (7, "Sujeción"),
        (8, 'Golpeo'),
        (9, 'Seguridad'),
        (10, "Marcación"),
        (11, "Medición"),
    )
    nombre=models.CharField(max_length=50, unique=True, choices=CLASES_HERRAMIENTAS)
    creado_por=models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        verbose_name='Clase de herramienta'
        verbose_name_plural='Clases de herramientas'
        
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "/{0}/".format(self.nombre)


class TipoHerramienta(models.Model):
    """ Tipo o nombre genérico. P. ej. serrucho, dentro del cual hay muchos, como de corte fino, de costilla, etc. No toda herramienta requiere un tipo, pero los tipos son únicos.
    """
    clase=models.ForeignKey(ClaseHerramienta)
    nombre=CharField(max_length=50, unique=True)
    creado_por=models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name='Tipo de herramienta'
        verbose_name_plural='Tipos de herramientas'
        
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return '/tipo/{0}'.format(self.nombre)


class ImagenHerramienta(models.Model):
    imagen = models.ImageField(upload_to='herramientas')
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    url = models.URLField(  blank=True)
    licencia = models.TextField()
    
    class Meta:
        verbose_name="Imagen"
        verbose_name_plural="Imágenes"
        
    def __unicode__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.imagen
        
        
class HerramientaGenerica(models.Model):
    """ Una herramienta de la cual distintas marcas hacen versiones. E. g. Cepillo #5 o Formón media caña para torno o Sierra circular.
    """
    clase=models.ForeignKey(ClaseHerramienta, help_text="Clase de herramienta.")
    tipo=models.ForeignKey(TipoHerramienta, blank=True, help_text="Tipo o nombre genérico. E.g. Serruco, el cual es el tipo de ´de corte fino´, ´de costilla´, etc.")
    nombre=models.CharField(max_length=100)
    nombre_corto=models.SlugField(max_length=30)
    imagenes=models.ManyToManyField(
        ImagenHerramienta,
        through='HerramientasGenericasImagenesHerramientas',
        upload_to="herramientas",
        blank=True,
        default="herramienta.png"
        )
    
    class Meta:
        verbose_name='Herramienta tipo'
        verbose_name_plural='Herramientas tipo'
        
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return 'herramientas/{0}/'.format(self.id)
    
    
class Marca(models.Model):
    nombre=models.CharField(max_length=100)
    pagina_web=models.URLField(blank=True)

    class Meta:
        verbose_name='Marca'
        verbose_name_plural='Marcas'
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre


class Herramienta(models.Model):
    herramienta_generica=models.ForeignKey(HerramientaGenerica, help_text="Herramienta genérica de la cual esta es una instancia. E.g. un serrucho de corte fino marca Veritas es una instancia de un Serrucho de corte fino.")
    marca=models.ForeignKey(Marca)
    modelo=models.CharField(max_length=150)
    detalle=models.CharField(max_length=255, blank=True)
    notas=models.TextField(blank=True)
    imagenes=models.ManyToManyField(
        ImagenHerramienta,
        through='HerramientasImagenesHerramientas',
        upload_to="herramientas",
        blank=True,
        default="herramienta.png"
        )
    
    class Meta:
        verbose_name='Herramienta'
        verbose_name_plural='Herramientas'
        
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return 'herramientas/{0}/'.format(self.id)


class Coleccion(models.Model):
    """Grupo de herramientas seleccionado o recomendado. Colección personal."""
    #Atributos básicos
    nombre=models.CharField(max_length=150)
    herramientas_genericas=models.ManyToManyField(
        HerramientaGenerica,
        through='ColeccionHerramientaGenerica',
        help_text=''
        )
    herramientas_recomendadas=models.ManyToManyField(
        Herramienta,
        through='ColeccionHerramientaRecomendada',
        blank=True
        )
    notas=models.TextField(blank=True)
    #Atributos opcionales
    creador=models.CharField(
        max_length=150,
        blank=True,
        help_text="Diseñador o creador original de esta colección. Ej. Chris Schwarz para ´The Anarchist's Toolchest´. Dejar en blanco si es igual al autor.")
    url=models.URLField(blank=True)
    url_creador=models.URLField(blank=True)
    #Metadatos
    autor=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        help_text="Autor del recurso en el sistema. ")
    fecha_creacion = models.DateField()
    fecha_actualizacion = models.DateField()
    
    class Meta:
        verbose_name=''
        verbose_name_plural=''
        ordering=['nombre']
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return "coleccion/{0}".format(self.id)


class HerramientasGenericasImagenesHerramientas(models.Model):
    imagen_herramienta=models.ForeignKey(ImagenHerramienta)
    herramienta_generica=models.ForeignKey(HerramientaGenerica)
    
    class Meta:
        verbose_name="Relación entre herramienta genérica e imagen"
        verbose_name_plural="Relaciones entre herramientas genéricas e imágenes"
        
    def __unicode__(self):
        return "{0}-{1}".format(self.herramienta_generica, self.imagen_herramienta)
    
class HerramientasImagenesHerramientas(models.Model):
    imagen_herramienta=models.ForeignKey(ImagenHerramienta)
    herramienta=models.ForeignKey(HerramientaGenerica)
    
    class Meta:
        verbose_name="Relación entre una herramienta y una imagen"
        verbose_name_plural="Relaciones entre herramientas e imágenes"
        
    def __unicode__(self):
        return "{0}-{1}".format(self.herramienta, self.imagen_herramienta)


class ColeccionHerramientaGenerica(models.Model):
    coleccion=models.ManyToManyField(Coleccion)
    herramienta_generica=models.Manager(HerramientaGenerica)
    requerida=models.BooleanField(default=True)
    notas=models.TextField(blank=True, help_text="Notas sobre la herramienta en la colección. E.g. Mantener varias cuchillas con distintos radios y ángulos a la mano para este cepillo. ")
    
    class Meta:
        verbose_name="Relación entre una colección y una herramienta genérica"
        verbose_name_plural="Relaciones entre colecciones y herramientas genéricas"
        
    def __unicode__(self):
        return "{0}-{1}".format(self.herramienta, self.imagen_herramienta)


class ColeccionHerramientaRecomendada(models.Model):
    coleccion=models.ManyToManyField(Coleccion)
    herramienta=models.Manager(Herramienta)
    recomendada_para=models.ForeignKey(ColeccionHerramientaGenerica)

    class Meta:
            verbose_name="Relación entre una colección y una herramienta"
            verbose_name_plural="Relaciones entre colecciones y herramientas"
        
    def __unicode__(self):
        return "{0}-{1}".format(self.herramienta, self.coleccion)




