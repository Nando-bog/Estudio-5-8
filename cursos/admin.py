#coding=utf-8
from django.contrib import admin
from cursos.models import Recurso, HiloConductor, TopicoGenerativo, MetaDeComprension, DesempenoDeComprension, Curso, HilosConductoresCurso, TopicosGenerativosCurso, MetasDeComprensionCurso, DesempenosCurso

class HilosConductoresCursoInline(admin.TabularInline):
    model = HilosConductoresCurso
    extra = 1
    
class TopicosGenerativosCursoInline(admin.TabularInline):
    model = TopicosGenerativosCurso
    extra = 1
    
class MetasDeComprensionCursoInline(admin.TabularInline):
    model = MetasDeComprensionCurso
    extra = 1

class DesempenosCursoInline(admin.TabularInline):
    model = DesempenosCurso
    extra = 1

class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'adjunto', 'url', 'tipo')
    filter_horizontal = ['autor',]
    prepopulated_fields = {'nombre_corto': ('nombre',)}
    fieldsets = (
        (None, {'fields': ('nombre', 'nombre_corto', 'url', 'tipo', 'adjunto', 'html', 'autor')}),
    )

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
        ("Información básica", {'fields': ('nombre', 'duracion',)}),
        ("Cuerpo", {'fields': ('cuerpo',)}),
        ("Recursos", {'fields': ('recursos',),'classes': ('collapse',)}),
        ("Metadatos", {'fields': ( 'autor', 'fecha_publicacion', 'fecha_actualizacion', 'tags', 'notas_profesor' ), 'classes' : ('collapse', )}),
    )
    inlines = (DesempenosCursoInline,)
    #fieldsets= (
    #    ("Información básica", {'fields': ('nombre', 'duracion', 'autor')}),
    #    ('Recursos', {'fields': ('recursos'), 'classes': ('collapse',)}),
    #    ('Cuerpo', {'fields': ('html',)}),
    #    ('Meta', {'fields': ('fecha_publicacion', 'fecha_actualizacion', 'tags', 'notas_profesor')})
    #)
    
    filter_horizontal=['autor', 'recursos',]

class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    filter_horizontal = ['profesores', 'inscritos', 'hilos_conductores', 'topicos_generativos', 'metas_de_comprension',]
    inlines = (HilosConductoresCursoInline, TopicosGenerativosCursoInline, MetasDeComprensionCursoInline, DesempenosCursoInline )
    #fieldsets = (
    #    ("Información´ básica", {'fields':('codigo', 'nombre', 'acceso', 'cupos', 'imagen_destacada',)}),
    #    ('Profesores', {'fields':('profesores',)}),
    #    ('Inscritos', {'fields':('inscritos',)}),
    #    ("Diseño curricular", {'fields':('hilos_conductores','topicos_generativos', 'metas_de_comprension',)}),        
    #)

admin.site.register(Recurso, RecursoAdmin)
admin.site.register(HiloConductor, HiloConductorAdmin)
admin.site.register(TopicoGenerativo, TopicoGenerativoAdmin)
admin.site.register(MetaDeComprension, MetaDeComprensionAdmin)
admin.site.register(DesempenoDeComprension, DesempenoDeComprensionAdmin)
admin.site.register(Curso, CursoAdmin)
