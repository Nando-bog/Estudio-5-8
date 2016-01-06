#coding=utf-8
# Admin para aplicación Roubo
# VERSION 0.12

from django.contrib import admin
from .models import Recurso, RecursosAutores, Destacado, Contacto #, HiloConductor, TopicoGenerativo, MetaCom, Desempeno, Curso,  DesempenosAutores, DesempenosRecursos, CursosProfesores, CursosHilosConductores, CursosTopicosGenerativos, CursosMetas, CursosDesempenos, Criterio, CriteriosMetas
# class CursosHilosConductoresInline(admin.TabularInline):
#     model = CursosHilosConductores
#     extra = 1
#     
#     
# class CursosTopicosGenerativosInline(admin.TabularInline):
#     model = CursosTopicosGenerativos
#     extra = 1
#     
#     
# class CursosMetasInline(admin.TabularInline):
#     model = CursosMetas
#     extra = 1
# 
# 
# class CursosDesempenosInline(admin.TabularInline):
#     model = CursosDesempenos
#     extra = 1
# 
# 
# class CursosProfesoresInline(admin.TabularInline):
#     model = CursosProfesores
#     extra = 1
# 
# 
class RecursosAutoresInline(admin.TabularInline):
    model = RecursosAutores
    extra = 1
# 
#     
# class DesempenosAutoresInline(admin.TabularInline):
#     model = DesempenosAutores
#     extra = 1
# 
#     
# class DesempenosRecursosInline(admin.TabularInline):
#     model = DesempenosRecursos
#     extra = 1


class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'url', 'tipo')
    prepopulated_fields = {'nombre_corto': ('nombre',)}
    fieldsets = (
        (None, {'fields': ('nombre', 'imagen_destacada', 'nombre_corto', 'fecha_creacion', 'fecha_actualizacion', 'url', 'tipo', 'cuerpo', 'tags')}),
    )
    inlines = (RecursosAutoresInline,)


class DestacadoAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'orden', 'sticky')
    
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'autor', 'email', 'url', 'texto')
# class HiloConductorAdmin(admin.ModelAdmin):
#     list_display=('nombre_corto', 'nombre')
#     prepopulated_fields = {'nombre_corto': ('nombre',)}
# 
# 
# class TopicoGenerativoAdmin(admin.ModelAdmin):
#     list_display=('nombre_corto', 'nombre')
#     prepopulated_fields = {'nombre_corto': ('nombre',)}
# 
# 
# class MetaAdmin(admin.ModelAdmin):
#     list_display=('nombre_corto', 'nombre')
#     prepopulated_fields = {'nombre_corto': ('nombre',)}
# 
# 
# class DesempenoAdmin(admin.ModelAdmin):
#     fieldsets = (
#         ("Información básica", {'fields': ('nombre', 'duracion', 'imagen_destacada')}),
#         ("Cuerpo", {'fields': ('cuerpo',)}),
#         ("Metadatos", {'fields': ( 'fecha_creacion', 'fecha_actualizacion', 'tags', 'notas_profesor' ),}),
#     )
#     inlines = (CursosDesempenosInline, DesempenosAutoresInline, DesempenosRecursosInline)    
#     filter_horizontal=['autor', 'recursos',]
# 
# 
# class CursoAdmin(admin.ModelAdmin):
#     list_display = ('codigo', 'nombre')
#     #filter_horizontal = ['profesores', 'hilos_conductores', 'topicos_generativos', 'metas_de_comprension', 'inscritos']
#     fieldsets = (
#         ("Información´ básica: ", {'fields':('codigo', 'nombre', 'acceso')}),
#         ("Si requiere inscripción: ", {'fields':('cupos', 'fecha_inicio')}),
#         ("Metadatos: ", {'fields': ('tags', 'imagen_destacada', )}),
#     )
#     inlines = (CursosHilosConductoresInline, CursosTopicosGenerativosInline, CursosMetasInline, CursosDesempenosInline, CursosProfesoresInline)
    
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Destacado, DestacadoAdmin)
admin.site.register(Contacto, ContactoAdmin)
#admin.site.register(HiloConductor, HiloConductorAdmin)
#admin.site.register(TopicoGenerativo, TopicoGenerativoAdmin)
#admin.site.register(MetaCom, MetaAdmin)
#admin.site.register(Desempeno, DesempenoAdmin)
#admin.site.register(Curso, CursoAdmin)
