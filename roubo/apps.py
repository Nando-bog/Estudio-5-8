#conding=utf-8

from django.apps import AppConfig
import watson

class RouboConfig(AppConfig):
    """Configuración para el app roubo.
    """
    
    name = 'roubo'
    
    def ready(self):
        recurso = self.get_model('Recurso')
        watson.search.register(
            recurso,
            fields = ('nombre', 'nombre_corto', 'fecha_creacion', 'fecha_actualizacion', 'cuerpo', 'tags'),
            store = ('cuerpo', 'nombre', 'fecha_creacion', 'fecha_actualizacion')
        )