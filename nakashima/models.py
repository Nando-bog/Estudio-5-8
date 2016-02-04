# coding = utf-8
# Modelos para la aplicación "Nakashima".
# VERSION 0.1

# Standard Python/Django libraries
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
from django.db import models
# Third party libraries
# Local libraries


def change_uploaded_filename(instance, filename):
    """Return a path and filename to upload an image."""

    upload_to = "nakashima-imagenes"
    extension = filename.split('.')[-1]
    filename = '{0}.{1}'.format(uuid4().hex, extension)
    return os.path.join(upload_to, filename)


class Imagen(models.Model):
    imagen = models.ImageField(blank=True, upload_to=change_uploaded_filename)
    autor = models.CharField(max_length=150, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"
        ordering = ['pk']

    def __str__(self):
        if self.nombre:
            return self.nombre
        else:
            return self.imagen


class Objeto(models.Model):
    """Representa un mueble, proyecto, artesanía."""
    # Constantes
    BIBLIOTECA = 'BIB'
    CAJA = 'CAJ'
    COCINA = 'COC'
    ENTRETENIMIENTO = 'ENT'
    ESCRITORIO = 'ESC'
    MESA = 'MES'
    PUERTA = 'PUE'
    SILLA = 'SIL'
    TORNO = 'TOR'
    OTRO = 'OTRO'

    TIPOS_OBJETO = (
        (BIBLIOTECA, 'Biblioteca'),
        (CAJA, 'Caja'),
        (COCINA, 'Cocina'),
        (ENTRETENIMIENTO, 'Centro de entretenimiento'),
        (ESCRITORIO, 'Escritorio'),
        (MESA, 'Mesa'),
        (SILLA, 'Silla'),
        (TORNO, 'Torno'),
        (OTRO, 'Otro'),
    )
    # Atributos basicos y obligatorios
    fecha_creacion = models.DateField(default=datetime.date.today)
    tipo = models.CharField(max_length=5, unique=True, choices=TIPOS_OBJETO)
    dimensiones = models.CharField(max_length=250)
    material = models.CharField(max_length=250)
    descripcion = models.TextField()
    rango_precio_bajo = models.IntegerField()
    rango_precio_alto = models.IntegerField()
    fecha_requerido = models.DateField(default=datetime.date.today + datetime.timedelta(days=14))
    entregado_artesano = models.BooleanField(default=False)
    entregado_cliente = models.BooleanField(default=False)

    # Atributos básico no obligatorios
    fecha_entregado = models.DateField(default=datetime.date.today + datetime.timedelta(days=14), blank=True)
    artesano = settings.AUTH_USER_MODEL(blank=True)
    cliente = settings.AUTH_USER_MODEL(blank=True, unique=True)
    cotizacion_aceptada = models.ForeighKey('Cotizacon', unique=True, blank=True)
    imagenes = models.ManyToManyField(Imagen, through='ObjetosImagenes', blank=True)

    class Meta:
        verbose_name = 'Objeto'
        verbose_name_plural = 'Objetos'
        ordering = ['fecha_entrega', 'fecha_creacion']

    def __str__():
        return '{0} código {1}'.format(self.tipo, self.pk)


class Cotizacion(models.Model):
    """Propuesta de objeto con precio hecha por un artesano a un cliente."""

    # Atributos básicos y obligatorios
    objeto = models.ForeighKey(Objeto, unique=True)
    artesano = models.ForeignKey(settings.AUTH.USER.MODEL, unique=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_actualizacion = models.DateField(default=datetime.date.today)
    models.DateField(default=datetime.date.today + datetime.timedelta(days=14))
    material = models.CharField(max_length=250)
    descripcion = models.TextField()
    precio = models.IntegerField()


class Portafolio(models.Model):
    """Portafolio de un artesano."""

    artesano = models.ForeighKey(settings.AUTH.USER.MODEL, unique=True)
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_actualizacion = models.DateField(default=datetime.date.today)
    proyectos = models.ManyToManyField(Objeto, blank=True, through='PortafoliosObjetos')
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['artesano', 'pk']

    def __str__():
        return 'Portafolio de '.format(self.artesano)


class AvanceObjeto(models.Model):
    """Reporte de avance de un objeto enviado por un artesano."""

    fecha_creacion = models.DateField(default=datetime.date.today)
    objeto = models.ForeignKey(Objeto)
    descripcion = models.TextField()
    imagenes = models.ManyToManyField(Imagen, through='AvancesObjetosImagenes', blank=True)

    class Meta:
        ordering = ['fecha_creacion']


class EvaluacionArtesano(models.Model):
    """Evaluación hecha por un cliente a un artesano que le hizo un proyecto."""

    fecha_creacion = models.DateField(default=datetime.date.today)
    artesano = models.ForeighKey(settings.AUTH.USER.MODEL, unique=True)
    cliente = models.ForeighKey(settings.AUTH.USER.MODEL, unique=True)
    objeto = models.ForeignKey(Objeto)
    calificacion = models.IntegerField()
    comentario = models.TextField()

    class Meta:
        ordering = ['artesano', 'fecha_creacion']

    def __str__(self):
        return 'Evaluación de {0}, {1}'.format(artesano, fecha_creacion)


class ObjetosImagenes(models.Model):
    pass


class PortafoliosObjetos(models.Model):
    pass


class AvancesObjetosImagenes(models.Model):
    pass
