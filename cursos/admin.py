from django.contrib import admin
from cursos.models import Curso, Leccion, Recurso

admin.site.register(Recurso)
admin.site.register(Curso)
admin.site.register(Leccion)
