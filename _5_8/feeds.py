#coding=utf-8
#Feeds de todo el sitio de Estudio 5-8

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from roubo.models import Recurso
from studley.models import TipoHerramienta, HerramientaBase, Herramienta, Coleccion
# import settings

class FeedItem:
    """Object with feed item attributes. Used to construct feed of items from multiple sections of the site.
    """
    def __init__(self, titulo, cuerpo, autores, fecha_actualizacion, tags, url_item, url_imagen):
        self.titulo = titulo
        self.cuerpo = cuerpo
        self.autores = autores
        self.fecha_actualizacion = fecha_actualizacion
        self.tags = tags
        self.url_imagen = url_imagen
        self.url_item = url_item
        
    def __lt__(self, other):
        return self.fecha_actualizacion < other.fecha_actualizacion
    
    
class SiteFeed(Feed):
    """Feed RSS de todo el sitio. Incluye el contenido nuevo de Studley y Roubo: herramientas y entradas de blog.
    """
    
    title = 'Estudio 5-8'
    link = '/rss/'
    description = 'Publicaciones del taller que comienza cuando el trabajo de 8-5 termina.'
    # item_enclosures_mime_type = "image/jpeg"
    
    def items(self, request):
        items_feed = []
        blogs = Recurso.objects.all().order_by('-fecha_actualizacion')
        tipos_herramientas = TipoHerramienta.objects.all().order_by('-fecha_actualizacion')
        herramientas = HerramientaBase.objects.all().order_by('-fecha_actualizacion')
        versiones_herramientas = Herramienta.objects.all().order_by('fecha_actualizacion')
        for blog in blogs:
            items_feed.append(FeedItem(blog.nombre, blog.cuerpo, 'autores', blog.fecha_actualizacion, '', blog.get_absolute_url(), blog.imagen_destacada))
        for tipo_herramienta in tipos_herramientas:
            items_feed.append(FeedItem(tipo_herramienta.nombre, tipo_herramienta.descripcion, tipo_herramienta.creado_por, tipo_herramienta.fecha_actualizacion, '', tipo_herramienta.get_absolute_url(), tipo_herramienta.imagen.imagen))
        for herramienta in herramientas:
            items_feed.append(FeedItem(herramienta.nombre, herramienta.descripcion, herramienta.creado_por, herramienta.fecha_actualizacion, '', herramienta.get_absolute_url(), herramienta.imagenes.all()[0].imagen))
        for version_herramienta in versiones_herramientas:
            items_feed.append(FeedItem(version_herramienta.__str__(), version_herramienta.detalle, version_herramienta.creado_por, version_herramienta.fecha_actualizacion, '', version_herramienta.get_absolute_url(), version_herramienta.imagenes.all()[0].imagen))
        return sorted(items_feed)
    
    def item_title(self, item):
        return item.titulo
    
    def item_link(self, item):
        return item.url_item
    
    def item_description(self, item):
        return item.cuerpo[:800]

    # def item_author_name(self, item ):
    #     pass
    # 
    # def item_updateddate(self, item ):
    #     return item.fecha_actualizacion
    # 
    # def item_categories(self, item):
    #     pass
    
    
    # def item_enclosure_url(self, item):
    #     return '{0}{1}'.format(settings.MEDIA_URL, (item.image_destacada))
