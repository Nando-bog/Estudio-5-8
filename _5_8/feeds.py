#coding=utf-8
#Feeds de todo el sitio de Estudio 5-8

from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from roubo.models import Recurso

class SiteFeed(Feed):
    """Feed RSS de todo el sitio. Incluye el contenido nuevo de Studley y Roubo: herramientas y entradas de blog.
    """
    
    title = 'Estudio 5-8'
    link = '/rss/'
    description = 'Publicaciones del taller que comienza cuando el trabajo de 8-5 termina.'
    item_enclosures_mime_type = "image/jpeg"
    
    def items(self, request):
        blogs = Recurso.objects.all().order_by('-fecha_actualizacion')
        return blogs
    
    def item_title(self, item):
        return item.nombre
    
    def item_description(self, item):
        return item.cuerpo[:800]
        
    def item_enclosure_url(self, item, request):
        return request.build_absolute_uri(item.image_destacada)
