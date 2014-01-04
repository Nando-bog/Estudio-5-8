#coding=utf-8
# Modelos para la aplicaci—n "Studley", una caja de herramientas.
# Cambiar de nombre y separar la caja de herramientas personal y prŽstamos del inventario... la caja de herramientas ser‡ Studley... las herramientas deben tener nombre de herrero... vulcano...
# Version 0.1
from django.db import models

class ClaseHerramienta(models.Model):
    """Clase de harramienta segœn su funci—n: Alisado, Atornillado, Corte, Labrado, Perforaci—n, Sujeci—n, Afilado, Golpeo, Seguridad, Marcaci—n, Medici—n, Aseo
    """
    CLASES_HERRAMIENTAS = (
        (1, 'Afilado'),
        (1, 'Alisado'),
        (2, 'Atornillado'),
        (3, 'Aseo'),
        (4, 'Corte'),
        (5, 'Labrado'),
        (6, "Perforaci—n"),
        (7, "Sujeci—n"),
        (8, 'Golpeo'),
        (9, 'Seguridad'),
        (10, "Marcaci—n"),
        (11, "Medici—n"),
    )
    nombre=models.CharField(max_length=50, unique=True, choices=CLASES_HERRAMIENTAS)
    
    
class TipoHerramienta(models.Model):
    """ Tipo o nombre genŽrico. P. ej. serrucho, dentro del cual hay muchos, como de corte fino, de costilla, etc. No toda herramienta requiere un tipo, pero los tipos son œnicos.
    """
    clase=models.ForeignKey(ClaseHerramienta)
    nombre=CharField(max_length=50, unique=True)


class ImagenHerramienta(models.Model):
    imagen = models.ImageField(upload_to='herramientas')
    autor = models.CharField(max_length=50)
    url = models.URLField()
    
    
class HerramientaGenerica(models.Model):
    """ Una herramienta puntual, de la cual distintas marcas hacen versiones. E. g. Cepillo #5 o Form—n media ca–a para torno.
    """
    clase=models.ForeignKey(ClaseHerramienta, help_text="Clase de herramienta.")
    tipo=models.ForeignKey(TipoHerramienta, blank=True, help_text="Tipo o nombre genŽrico. E.g. Serruco, el cual es el tipo de «de corte fino«, «de costilla«, etc.")
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


class Herramienta(models.Model):
    herramienta_generica=models.ForeignKey(HerramientaGenerica, help_text="Herramienta genŽrica de la cual esta es una instancia. E.g. un serrucho de corte fino marca Veritas es una instancia de un Serrucho de corte fino.")
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
    nombre=models.CharField(max_length=150)
    creador=models.CharField(max_length=150)
    url=models.URLField(blank=True)
    url_creador=models.URLField(blank=True)
    herramientas_genericas=models.ManyToManyField(HerramientaGenerica, through='ColeccionHerramientaGenerica')
    herramientas_recomendadas=models.ManyToManyField(Herramienta, through='ColeccionHerramientaRecomendada', blank=True)


class HerramientasGenericasImagenesHerramientas(models.Model):
    imagen_herramienta=models.ForeignKey(ImagenHerramienta)
    herramienta_generica=models.ForeignKey(HerramientaGenerica)


class HerramientasImagenesHerramientas(models.Model):
    imagen_herramienta=models.ForeignKey(ImagenHerramienta)
    herramienta=models.ForeignKey(HerramientaGenerica)


class ColeccionHerramientaGenerica(models.Model):
    coleccion=models.ManyToManyField(Coleccion)
    herramienta_generica=models.Manager(HerramientaGenerica)
    requerida=models.BooleanField(default=True)


class ColeccionHerramientaRecomendada(models.Model):
    coleccion=models.ManyToManyField(Coleccion)
    herramienta=models.Manager(Herramienta)
    recomendada_para=models.ForeignKey(ColeccionHerramientaGenerica)






