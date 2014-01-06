#coding=utf-8
# Admin para aplicación Studley
# VERSION 0.1
from django.contrib import admin
from .models import HerramientaBase, Herramienta, Coleccion, ClaseHerramienta, TipoHerramienta, Imagen

admin.site.register(HerramientaBase)
admin.site.register(Herramienta)
admin.site.register(Coleccion)
admin.site.register(ClaseHerramienta)
admin.site.register(TipoHerramienta)
admin.site.register(Imagen)