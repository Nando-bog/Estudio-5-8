#coding=utf-8
#Scripts para poblar la base de datos con datos de prueba.
#Corre las FUNCIONES int(CANTIDAD) de veces. Cada función debe recibir un solo argumento, int(cantidad) y modificar la base de datos por su cuenta. Debe correr desde el shell del proyecto de Django.
import datetime
from django.contrib.auth.models import User
from taggit.models import Tag
from taggit.managers import TaggableManager
from studley.models import ClaseHerramienta, TipoHerramienta

CANTIDAD = 5
##TRAER EL PRIMER USUARIO REGISTRADO (ADMIN)
USUARIO=User.objects.all()[0]
#Texto de relleno
LOREM_IPSUM="<p>&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt erat at purus elementum, eget aliquet lorem bibendum. In sit amet rutrum lacus. Pellentesque vitae condimentum elit. Quisque laoreet, urna eu scelerisque blandit, arcu neque ornare ante, vitae pellentesque est leo et lacus. Pellentesque auctor, sem sit amet volutpat mattis, velit nunc malesuada lacus, eget tincidunt sapien dui pretium leo. Proin viverra sapien velit, eget ultricies arcu semper eu. Fusce eget lacus bibendum, interdum nisl at, posuere risus. Curabitur feugiat diam eget tellus faucibus tempus.</p> <p>Vestibulum sed nunc mauris. Duis faucibus metus sed egestas malesuada. Nunc mattis orci ut metus adipiscing, eu cursus augue faucibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed condimentum elementum accumsan. Aliquam nec porta dolor. In hac habitasse platea dictumst. Proin hendrerit justo nulla, non hendrerit ligula gravida ac. Phasellus at libero metus. Aliquam mi elit, congue fermentum aliquet quis, convallis eget enim. Sed sed enim in mauris malesuada rhoncus et vitae felis. Aenean facilisis cursus turpis, dapibus viverra orci pharetra a. Aliquam sodales, purus sit amet euismod sollicitudin, mauris mi ultrices justo, suscipit posuere nunc magna eleifend leo. Maecenas et nunc elementum nisi interdum tristique eget sit amet mauris. In tempus malesuada est, at eleifend nisl molestie in.</p><p>Mauris nec velit nec magna varius suscipit sit amet quis ipsum. Donec vulputate tristique rutrum. Nam gravida dui ut ante feugiat placerat. Vestibulum porttitor dapibus ante, molestie eleifend sem interdum id. Ut sodales rhoncus fringilla. Nullam iaculis facilisis tincidunt. Nunc pretium auctor felis at aliquet. Sed in venenatis dui. Quisque eu lectus ligula. Vivamus fringilla convallis dolor, vel ultrices est congue vel. Vivamus lectus tortor, posuere ut fringilla ac, sollicitudin quis mauris. Duis et accumsan ipsum, at hendrerit lorem.</p><p>In consectetur scelerisque tellus, eget sollicitudin risus imperdiet in. Phasellus quis elit consequat, porttitor metus in, interdum ipsum. Aenean sit amet commodo est. Etiam est turpis, congue bibendum vehicula non, mollis vel dui. Sed tincidunt lectus eget ligula volutpat, vitae ornare risus hendrerit. Aliquam scelerisque pellentesque iaculis. Quisque ac arcu quis risus molestie tempus ac eget ante. Duis in est eu sapien mattis euismod nec a quam. Pellentesque vitae erat venenatis, convallis ipsum eget, convallis erat. Curabitur in ante eget ipsum elementum varius pulvinar vel turpis. Nullam pulvinar nisl at ligula viverra laoreet ac eu nulla.&nbsp;</p>"


def poblar(cantidad, funciones):
    """
    int(cantidad), list(funciones)
    Funciones solamente pueden recibir un int(cantidad)
    """
    for f in funciones:
        print f, cantidad
        f(cantidad)

def crear_clases_herramientas(cantidad):
    """
    Crea todas las clases de herramientas predefinidas.
    """
    for clase in ClaseHerramienta.CLASES_HERRAMIENTAS:
        ClaseHerramienta(nombre=clase[1], descripcion=LOREM_IPSUM, creado_por=USUARIO).save()

def crear_tipos_herramientas(cantidad):
    """
    Crea todas las clases de herramientas predefinidas.
    """
    for clase_herramienta in ClaseHerramienta.objects.all():
        TipoHerramienta(clase=clase_herramienta, nombre='Nombre herramienta {0}'.format(clase_herramienta), creado_por=USUARIO).save()
    

FUNCIONES = [crear_tipos_herramientas]

poblar(CANTIDAD,FUNCIONES)