#coding=utf-8
#Scripts para poblar la base de datos con datos de prueba.
#Corre las FUNCIONES int(CANTIDAD) de veces. Cada función debe recibir un solo argumento, int(cantidad) y modificar la base de datos por su cuenta. Debe correr desde el shell del proyecto de Django.
import datetime
from django.contrib.auth.models import User
#from taggit.models import Tag
#from taggit.managers import TaggableManager
from studley.models import ClaseHerramienta, TipoHerramienta
CANTIDAD = 5
##TRAER EL PRIMER USUARIO REGISTRADO (ADMIN)
USUARIO=User.objects.all()[0]
#Texto de relleno
LOREM_IPSUM="<p>&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt erat at purus elementum, eget aliquet lorem bibendum. In sit amet rutrum lacus. Pellentesque vitae condimentum elit. Quisque laoreet, urna eu scelerisque blandit, arcu neque ornare ante, vitae pellentesque est leo et lacus. Pellentesque auctor, sem sit amet volutpat mattis, velit nunc malesuada lacus, eget tincidunt sapien dui pretium leo. Proin viverra sapien velit, eget ultricies arcu semper eu. Fusce eget lacus bibendum, interdum nisl at, posuere risus. Curabitur feugiat diam eget tellus faucibus tempus.</p> <p>Vestibulum sed nunc mauris. Duis faucibus metus sed egestas malesuada. Nunc mattis orci ut metus adipiscing, eu cursus augue faucibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed condimentum elementum accumsan. Aliquam nec porta dolor. In hac habitasse platea dictumst. Proin hendrerit justo nulla, non hendrerit ligula gravida ac. Phasellus at libero metus. Aliquam mi elit, congue fermentum aliquet quis, convallis eget enim. Sed sed enim in mauris malesuada rhoncus et vitae felis. Aenean facilisis cursus turpis, dapibus viverra orci pharetra a.</p>"


def poblar(cantidad, funciones):
    """
    int(cantidad), list(funciones)
    Funciones solamente pueden recibir un int(cantidad)
    """
    for f in funciones:
        for i in range(cantidad):
            f()
            print(f, cantidad)

def crear_clases_herramientas():
    """
    Crea todas las clases de herramientas predefinidas.
    """
    for clase in ClaseHerramienta.CLASES_HERRAMIENTAS:
        ClaseHerramienta(nombre=clase[1], descripcion=LOREM_IPSUM, creado_por=USUARIO).save()

def crear_tipos_herramientas():
    """
    Crea todas las clases de herramientas predefinidas.
    """
    counter = 5
    for clase_herramienta in ClaseHerramienta.objects.all():
        TipoHerramienta(clase=clase_herramienta, nombre='{0}{1}'.format(clase_herramienta.__str__(), str(counter)), creado_por=USUARIO).save()
        counter += 1


FUNCIONES = [crear_clases_herramientas, crear_tipos_herramientas]

#poblar(CANTIDAD, FUNCIONES)