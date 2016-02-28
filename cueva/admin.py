# coding=utf-8
# Admin para aplicación CUEVA
# VERSION 0.1

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import DestacadoHome, ImagenFondoHome


# class DestacadoHomeAdminInline(GenericTabularInline):
#     

class DestacadoHomeAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'contenido_destacado', 'orden', 'fecha_creacion', 'object_id')


class ImagenFondoHomeAdmin(admin.ModelAdmin):
    list_display = ('imagen', 'nombre', 'autor', 'url', 'licencia')


admin.site.register(DestacadoHome, DestacadoHomeAdmin)
admin.site.register(ImagenFondoHome, ImagenFondoHomeAdmin)
