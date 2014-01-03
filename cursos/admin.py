#coding=utf-8
# Admin para aplicación Cursos
# VERSION 0.12

from django.contrib import admin
from .models import Recurso, HiloConductor, TopicoGenerativo, MetaDeComprension, DesempenoDeComprension, Curso, RecursosAutores, DesempenosDeComprensionAutores, DesempenosDeComprensionRecursos, CursosProfesores, CursosHilosConductores, CursosTopicosGenerativos, CursosMetasDeComprension, CursosDesempenosDeComprension, CursosInscritos

class CursosHilosConductoresInline(admin.TabularInline):
    model = CursosHilosConductores
    extra = 1
    
class CursosTopicosGenerativosInline(admin.TabularInline):
    model = CursosTopicosGenerativos
    extra = 1
    
class CursosMetasDeComprensionInline(admin.TabularInline):
    model = CursosMetasDeComprension
    extra = 1

class CursosDesempenosDeComprensionInline(admin.TabularInline):
    model = CursosDesempenosDeComprension
    extra = 1

class CursosProfesoresInline(admin.TabularInline):
    model = CursosProfesores
    extra = 1

class CursosInscritosInline(admin.TabularInline):
    model = CursosInscritos
    extra = 1


class RecursosAutoresInline(admin.TabularInline):
    model = RecursosAutores
    extra = 1
    
class DesempenosDeComprensionAutoresInline(admin.TabularInline):
    model = DesempenosDeComprensionAutores
    extra = 1
    
class DesempenosDeComprensionRecursosInline(admin.TabularInline):
    model = DesempenosDeComprensionRecursos
    extra = 1

class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'adjunto', 'url', 'tipo')
    prepopulated_fields = {'nombre_corto': ('nombre',)}
    fieldsets = (
        (None, {'fields': ('nombre', 'imagen_destacada', 'nombre_corto', 'url', 'tipo', 'adjunto', 'cuerpo', 'tags')}),
    )
    inlines = (RecursosAutoresInline, DesempenosDeComprensionRecursosInline)

class HiloConductorAdmin(admin.ModelAdmin):
    list_display=('nombre_corto', 'nombre')
    prepopulated_fields = {'nombre_corto': ('nombre',)}

class TopicoGenerativoAdmin(admin.ModelAdmin):
    list_display=('nombre_corto', 'nombre')
    prepopulated_fields = {'nombre_corto': ('nombre',)}

class MetaDeComprensionAdmin(admin.ModelAdmin):
    list_display=('nombre_corto', 'nombre')
    prepopulated_fields = {'nombre_corto': ('nombre',)}

class DesempenoDeComprensionAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Información básica", {'fields': ('nombre', 'duracion', 'imagen_destacada')}),
        ("Cuerpo", {'fields': ('cuerpo',)}),
        ("Metadatos", {'fields': ( 'fecha_publicacion', 'fecha_actualizacion', 'tags', 'notas_profesor' ),}),
    )
    inlines = (CursosDesempenosDeComprensionInline, DesempenosDeComprensionAutoresInline, DesempenosDeComprensionRecursosInline)    
    filter_horizontal=['autor', 'recursos',]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    #filter_horizontal = ['profesores', 'hilos_conductores', 'topicos_generativos', 'metas_de_comprension', 'inscritos']
    fieldsets = (
        ("Información´ básica: ", {'fields':('codigo', 'nombre', 'acceso')}),
        ("Si requiere inscripción: ", {'fields':('cupos', 'fecha_inicio','fecha_fin',)}),
        ("Metadatos: ", {'fields': ('tags', 'imagen_destacada', )}),
    )
    inlines = (CursosHilosConductoresInline, CursosTopicosGenerativosInline, CursosMetasDeComprensionInline, CursosDesempenosDeComprensionInline, CursosInscritosInline, CursosProfesoresInline)
    
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(HiloConductor, HiloConductorAdmin)
admin.site.register(TopicoGenerativo, TopicoGenerativoAdmin)
admin.site.register(MetaDeComprension, MetaDeComprensionAdmin)
admin.site.register(DesempenoDeComprension, DesempenoDeComprensionAdmin)
admin.site.register(Curso, CursoAdmin)
