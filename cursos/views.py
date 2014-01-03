#coding=utf-8
# Views para la aplicación "Cursos"
#Version 0.1

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Recurso, DesempenoDeComprension, Curso

#Detalle de un recurso
class RecursoDetailView(DetailView):
    template_name = 'recurso_detalle.html'
    context_object_name = 'recurso'
    
    def get_object(self, **kwargs):
        self.recurso=get_object_or_404(Recurso, nombre_corto=self.kwargs['nombre_corto'])
        self.desempenos=self.recurso.desempenodecomprension_set.all()
        if len(self.desempenos)==0:
            self.desempenos="No hay desempeños asociados con este recurso."
        return self.recurso
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(RecursoDetailView, self).get_context_data(**kwargs)
        context['desempenos']=self.desempenos
        return context

#Detalle de un desempeño
class DesempenoDeComprensionDetailView(DetailView):
    template_name='desempeno_detalle.html'
    context_object_name='desempeno'
    
    def get_object(self, **kwargs):
        self.desempeno=get_object_or_404(DesempenoDeComprension, nombre_corto=self.kwargs['nombre_corto'])
        self.cursos=self.desempeno.curso_set.all()
        return self.desempeno
    
    def get_context_data(self, **kwargs ):
         # Call the base implementation first to get a context
        context = super(DesempenoDeComprensionDetailView, self).get_context_data(**kwargs)
        context['cursos']=self.cursos
        return context
    
#Detalle de un curso (página de inicio)
class CursoInicioDetailView(DetailView):
    template_name="curso_presentacion.html"
    model=Curso
    slug_field='codigo'
    slug_url_kwarg='codigo'

#Lista de cursos. Debe tener filtro y caja de búsqueda. Creo que sería con mixins y Javascript... phew...
class CursoListView(ListView):
    model=Curso
    context_object_name='cursos'
    template_name='cursos_lista_todos.html'

#Lista de recursos. Debe tener filtro y caja de búsqueda.
class RecursosListView(ListView):
    pass

#Lista de recursos por tipo (landing del tipo)
class RecursosTiposListView(ListView):
    pass

##Editar recurso
#Agregar recurso

