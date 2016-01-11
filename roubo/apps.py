from django.apps import AppConfig
# import watson

class RouboConfig(AppConfig):
    """
    """
    
    name = 'roubo'
    
    # def ready(self):
    #     recurso = self.get_model('Recurso')
    #     watson.register(
    #         recurso,
    #         fields = ('nombre', 'nombre-corto', 'fecha-creacion', 'fecha-actualizacion', 'cuerpo', 'tags'),
    #         exclude = ('imagen_destacada',),
    #         store = ('cuerpo', 'nombre', 'fecha_creacion', 'fecha_actualizacion', 'imagen_destacada')
    #     )