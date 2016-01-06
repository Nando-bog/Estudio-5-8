#coding=utf-8
# Modelos para la aplicación "Roubo", una caja de herramientas.
# La caja de herramientas personal de un usuario es una colección.
# Diseñar métodos para comparar, compartir, etc., colecciones. ¡Sigue siendo Studley!
# Version 0.13
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Imagen(models.Model):
    imagen = models.ImageField(upload_to='herramientas')
    nombre = models.CharField(max_length=150)
    autor = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)
    licencia = models.TextField(blank=True)
    
    class Meta:
        verbose_name="Imagen"
        verbose_name_plural="Imágenes"
        
    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.imagen
        

class ClaseHerramienta(models.Model):
    """Clase de herramienta según su función: Alisado, Corte,
    Labrado, Perforación y Sujeción, Afilado, Golpeo, Seguridad, Marcación y
    Medición, Aseo
    """
    CLASES_HERRAMIENTAS = (
    ##Actualizar este listado según nueva lista de clases...
    ##¿Sacar a una tabla propia las clases, dejar abierto?
        ('Acabados', 'Acabados'),
        ('Afilado', 'Afilado'),
        ('Alisado', 'Alisado'),
        ('Atornillado', 'Atornillado'),
        ('Aseo', 'Aseo'),
        ('Corte', 'Corte'),
        ('Labrado', 'Labrado'),
        ('Lijado', 'Lijado'),
        ("Marcacion", "Marcación y medición"),
        ("Perforacion", "Perforación"),
        ("Sujecion", "Sujeción"),
        ('Golpeo', 'Golpeo'),
        ('Seguridad', 'Seguridad'),   
    )
    nombre=models.CharField(max_length=50, unique=True, choices=CLASES_HERRAMIENTAS)
    descripcion=models.TextField()
    imagen=models.ForeignKey(Imagen, blank=True)
    creado_por=models.ForeignKey(settings.AUTH_USER_MODEL)
    
    class Meta:
        verbose_name='Clase'
        verbose_name_plural='Clases'
        
    class Admin:
        pass
    
    def __str__(self):
        return self.get_nombre_display()
    
    def get_absolute_url(self):
        #return "{0}".format(u'self.nombre')
        return reverse('herramienta_clase_detalle', kwargs={'nombre':self.nombre})


class TipoHerramienta(models.Model):
    """ Tipo o nombre genérico. P. ej. serrucho, dentro del cual hay muchos, como de corte fino, de costilla, etc. No toda herramienta requiere un tipo, pero es raro que una herramienta no sea parte de uno. Los tipos son únicos.
    """
    clase=models.ForeignKey(ClaseHerramienta)
    nombre=models.CharField(max_length=150, unique=True)
    nombre_plural=models.CharField(max_length=150)
    nombre_corto=models.SlugField(max_length=30, unique=True, help_text="Debe ser único.")
    imagen=models.ForeignKey(Imagen, blank=True)
    descripcion=models.TextField(blank=True)
    creado_por=models.ForeignKey(settings.AUTH_USER_MODEL)

    class Meta:
        verbose_name='Tipo'
        verbose_name_plural='Tipos'
        
    class Admin:
        pass
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse("herramienta_tipo_detalle", kwargs={'nombre_corto':self.nombre_corto})
    #     return '/tipo/{0}'.format(self.nombre)

        
class HerramientaBase(models.Model):
    """ Una herramienta de la cual distintas marcas hacen versiones. E. g. Cepillo #5 o Formón media caña para torno o Sierra circular.
    """
    clase=models.ForeignKey(ClaseHerramienta, help_text="Clase de herramienta.")
    tipo=models.ForeignKey(TipoHerramienta, blank=True, help_text="Tipo o nombre genérico. E.g. Serrucho, el cual es el tipo de ´de corte fino´, ´de costilla´, etc.")
    nombre=models.CharField(max_length=150)
    nombre_corto=models.SlugField(max_length=30, unique=True, help_text="Debe ser único.")
    imagenes=models.ManyToManyField(Imagen, through='HerramientasBaseImagenes', blank=True)
    descripcion=models.TextField(help_text='Describa la herramienta.')
    
    class Meta:
        verbose_name='Herramienta base'
        verbose_name_plural='Herramientas base'
        
    class Admin:
        pass
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        #return 'herramientas/{0}/'.format(self.nombre_corto)
        return reverse('herramienta_base_detalle', kwargs={'nombre_corto':self.nombre_corto})
    
    
class Marca(models.Model):
    """ Marca o fabricante de herramientas. P. ej. Stanley, Veritas, Lie-Nielsen."""
    nombre=models.CharField(unique=True, max_length=150)
    pagina_web=models.URLField(blank=True)

    class Meta:
        verbose_name='Marca'
        verbose_name_plural='Marcas'
    
    class Admin:
        pass
    
    def __str__(self):
        return self.nombre


class Herramienta(models.Model):
    """Instancia de una herramienta base, una combinación de marca, modelo y herramienta base.
    """
    herramienta_base=models.ForeignKey(HerramientaBase, help_text="Herramienta genérica de la cual esta es una instancia. E.g. un serrucho de corte fino marca Veritas es una instancia de un Serrucho de corte fino.")
    marca=models.ForeignKey(Marca)
    modelo=models.CharField(max_length=150)
    detalle=models.TextField(blank=True)
    notas=models.TextField(blank=True)
    imagenes=models.ManyToManyField(Imagen, through='HerramientasImagenes', blank=True)
    
    class Meta:
        verbose_name='Herramienta'
        verbose_name_plural='Herramientas'
        
    class Admin:
        pass
    
    def __str__(self):
        return self.herramienta_base.__str__() + " " + self.marca.nombre
    
    def get_absolute_url(self):
        return reverse('herramienta_version_detalle', kwargs={'pk': self.pk })
    #     return 'herramientas/herramienta/{0}/'.format(self.id)


class Coleccion(models.Model):
    """Grupo de herramientas seleccionado o recomendado. Colección personal."""
    #Atributos básicos
    nombre=models.CharField(max_length=150, unique=True)
    nombre_corto=models.SlugField(max_length=30, unique=True, help_text="Debe ser único.")
    imagenes=models.ManyToManyField(Imagen, through='ColeccionesImagenes', blank=True)
    herramientas_base=models.ManyToManyField(
        HerramientaBase,
        through='ColeccionesHerramientasBase',
        help_text='',
        blank=True
        )
    herramientas_recomendadas=models.ManyToManyField(
        Herramienta,
        through='ColeccionesHerramientas',
        blank=True
        )
    descripcion=models.TextField(blank=True)
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
        verbose_name="Colección"
        verbose_name_plural="Colecciones"
        ordering=['nombre']
    
    class Admin:
        pass
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('coleccion_detalle', kwargs={'nombre_corto': self.nombre_corto })
    #     return "coleccion/{0}".format(self.nombre)


class HerramientasBaseImagenes(models.Model):
    imagen_herramienta=models.ForeignKey(Imagen)
    herramienta_base=models.ForeignKey(HerramientaBase)
        
    def __str__(self):
        return "{0}-{1}".format(self.herramienta_base, self.imagen_herramienta)
    
    
class HerramientasImagenes(models.Model):
    imagen_herramienta=models.ForeignKey(Imagen)
    herramienta=models.ForeignKey(Herramienta)
        
    def __str__(self):
        return "{0}-{1}".format(self.herramienta, self.imagen_herramienta)


class ColeccionesHerramientasBase(models.Model):
    coleccion=models.ForeignKey(Coleccion)
    herramienta_base=models.ForeignKey(HerramientaBase)
    requerida=models.BooleanField(default=True)
    notas=models.TextField(blank=True, help_text="Notas sobre la herramienta en la colección. E.g. Mantener varias cuchillas con distintos radios y ángulos a la mano para este cepillo. ")
            
    def __str__(self):
        return "{0}-{1}".format(self.herramienta_base, self.coleccion)


class ColeccionesHerramientas(models.Model):
    coleccion=models.ForeignKey(Coleccion)
    herramienta=models.ForeignKey(Herramienta)
    recomendada_para=models.ForeignKey(ColeccionesHerramientasBase)
        
    def __str__(self):
        return "{0}-{1}".format(self.herramienta, self.coleccion)
    
class ColeccionesImagenes(models.Model):
    coleccion = models.ForeignKey(Coleccion)
    imagen_coleccion = models.ForeignKey(Imagen)
    
    def __str__(self):
        return "{0}".format(self.coleccion.nombre)