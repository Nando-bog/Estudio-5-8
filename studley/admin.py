#coding=utf-8
# Admin para aplicación Studley
# VERSION 0.1
from django.contrib import admin
from .models import HerramientaBase, Herramienta, Marca, Coleccion, ClaseHerramienta, TipoHerramienta, Imagen, HerramientasBaseImagenes, HerramientasImagenes, ColeccionesImagenes, ColeccionesHerramientasBase, ColeccionesHerramientas


class HerramientaBaseImagenInline(admin.TabularInline):
    model = HerramientasBaseImagenes
    extra = 1


class HerramientaBaseAdmin(admin.ModelAdmin):
    inlines = (HerramientaBaseImagenInline, )


class HerramientaImagenInline(admin.TabularInline):
    model = HerramientasImagenes
    extra = 1


class HerramientaAdmin(admin.ModelAdmin):
    inlines = (HerramientaImagenInline, )
    
    
class ColeccionImagenInline(admin.TabularInline):
    model = ColeccionesImagenes
    extra = 1
    
class ColeccionHerramientasBaseInline(admin.TabularInline):
    model = ColeccionesHerramientasBase
    extra = 1
    
class ColeccionHerramientasRecomendadasInline(admin.TabularInline):
    model = ColeccionesHerramientas
    extra = 0
    
class ColeccionAdmin(admin.ModelAdmin):
    inlines = (ColeccionImagenInline, ColeccionHerramientasBaseInline, ColeccionHerramientasRecomendadasInline)
    

admin.site.register(HerramientaBase, HerramientaBaseAdmin)
admin.site.register(Herramienta, HerramientaAdmin)
admin.site.register(Coleccion, ColeccionAdmin)
admin.site.register(ClaseHerramienta)
admin.site.register(TipoHerramienta)
admin.site.register(Imagen)
admin.site.register(Marca)