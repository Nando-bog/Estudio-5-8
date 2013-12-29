from django.contrib import admin
from cursos.models import Curso, Leccion, Recurso

class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'imagen_destacada')
    filter_horizontal = ['profesor',]
    
class RecursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'tipo', 'tags')
    filter_horizontal = ['autor']
    prepopulated_fields = {'nombre_corto': ('nombre',)}

admin.site.register(Curso, CursoAdmin)
admin.site.register(Recurso, RecursoAdmin)
admin.site.register(Leccion)
