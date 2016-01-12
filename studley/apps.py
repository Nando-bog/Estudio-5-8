#coding=utf-8

from django.apps import AppConfig
import watson

class StudleyConfig(AppConfig):
    name = 'studley'
    def ready(self):
        #Modelos para registrar en buscador *watson*
        clase_herramienta = self.get_model('ClaseHerramienta')
        tipo_herramienta = self.get_model('TipoHerramienta')
        herramienta_base = self.get_model('HerramientaBase')
        herramienta = self.get_model('Herramienta')
        marca = self.get_model('Marca')
        coleccion = self.get_model('Coleccion')
        #Registrar modelos y campos para buscar o excluir
        watson.search.register(
            clase_herramienta.objects.filter(publicado=True),
            fields=('nombre', 'descripcion', 'fecha_actualizacion'),
            store=('nombre', 'descripcion', 'fecha_actualizacion')
            )
        watson.search.register(
            tipo_herramienta.objects.filter(publicado=True),
            fields=('nombre', 'nombre_plural', 'nombre_corto', 'descripcion', 'fecha_actualizacion'),
            store=('nombre', 'descripcion', 'fecha_actualizacion')
            )
        watson.search.register(
            herramienta_base.objects.filter(publicado=True),
            fields=('clase', 'tipo', 'nombre', 'nombre_corto', 'descripcion', 'fecha_actualizacion'),
            store=('nombre', 'descripcion', 'fecha_actualizacion')
            )
        watson.search.register(
            marca.objects.filter(publicado=True),
            fields=('nombre', 'fecha_actualizacion'),
            store=('nombre', 'fecha_actualizacion')
            )
        watson.search.register(
            herramienta.objects.filter(publicado=True),
            fields = ('marca', 'modelo', 'detalle', 'notas', 'fecha_actualizacion'),
            store = ('modelo', 'detalle', 'fecha_actualizacion')
            )
        watson.search.register(
            coleccion.objects.filter(publicado=True),
            fields = ('nombre', 'nombre_corto', 'herramientas_recomendadas', 'descripcion', 'creador', 'url', 'url_creador', 'fecha_actualizacion'),
            store = ('nombre', 'descripcion', 'creador', 'fecha_actualizacion')
        )
        