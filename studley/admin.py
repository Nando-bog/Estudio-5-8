#coding=utf-8
# Admin para aplicación Studley
# VERSION 0.1
from django.contrib import admin
from .models import HerramientaBase, Herramienta, Coleccion, ClaseHerramienta, TipoHerramienta, Imagen, HerramientasBaseImagenes

class HerramientaBaseImagenInline(admin.TabularInline):
    model = HerramientasBaseImagenes
    extra = 1


class HerramientaBaseAdmin(admin.ModelAdmin):
    inlines = (HerramientaBaseImagenInline, )


admin.site.register(HerramientaBase, HerramientaBaseAdmin)
admin.site.register(Herramienta)
admin.site.register(Coleccion)
admin.site.register(ClaseHerramienta)
admin.site.register(TipoHerramienta)
admin.site.register(Imagen)