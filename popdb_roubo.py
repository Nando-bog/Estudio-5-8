#coding=utf-8
#Scripts para poblar la base de datos con datos de prueba.
#Corre las FUNCIONES int(CANTIDAD) de veces. Cada función debe recibir un solo argumento, int(cantidad) y modificar la base de datos por su cuenta. Debe correr desde el shell del proyecto de Django.
import datetime
from django.contrib.auth.models import User
from taggit.models import Tag
from taggit.managers import TaggableManager
from roubo.models import Recurso, HiloConductor, TopicoGenerativo, MetaDeComprension, DesempenoDeComprension, Curso, RecursosAutores, DesempenosDeComprensionAutores, DesempenosDeComprensionRecursos, CursosProfesores, CursosHilosConductores, CursosTopicosGenerativos, CursosMetasDeComprension, CursosDesempenosDeComprension

CANTIDAD = 5
##TRAER EL PRIMER USUARIO REGISTRADO (ADMIN)
USUARIO=User.objects.all()[0]
LOREM_IPSUM="<p>&nbsp;Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi tincidunt erat at purus elementum, eget aliquet lorem bibendum. In sit amet rutrum lacus. Pellentesque vitae condimentum elit. Quisque laoreet, urna eu scelerisque blandit, arcu neque ornare ante, vitae pellentesque est leo et lacus. Pellentesque auctor, sem sit amet volutpat mattis, velit nunc malesuada lacus, eget tincidunt sapien dui pretium leo. Proin viverra sapien velit, eget ultricies arcu semper eu. Fusce eget lacus bibendum, interdum nisl at, posuere risus. Curabitur feugiat diam eget tellus faucibus tempus.</p> <p>Vestibulum sed nunc mauris. Duis faucibus metus sed egestas malesuada. Nunc mattis orci ut metus adipiscing, eu cursus augue faucibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Sed condimentum elementum accumsan. Aliquam nec porta dolor. In hac habitasse platea dictumst. Proin hendrerit justo nulla, non hendrerit ligula gravida ac. Phasellus at libero metus. Aliquam mi elit, congue fermentum aliquet quis, convallis eget enim. Sed sed enim in mauris malesuada rhoncus et vitae felis. Aenean facilisis cursus turpis, dapibus viverra orci pharetra a. Aliquam sodales, purus sit amet euismod sollicitudin, mauris mi ultrices justo, suscipit posuere nunc magna eleifend leo. Maecenas et nunc elementum nisi interdum tristique eget sit amet mauris. In tempus malesuada est, at eleifend nisl molestie in.</p><p>Mauris nec velit nec magna varius suscipit sit amet quis ipsum. Donec vulputate tristique rutrum. Nam gravida dui ut ante feugiat placerat. Vestibulum porttitor dapibus ante, molestie eleifend sem interdum id. Ut sodales rhoncus fringilla. Nullam iaculis facilisis tincidunt. Nunc pretium auctor felis at aliquet. Sed in venenatis dui. Quisque eu lectus ligula. Vivamus fringilla convallis dolor, vel ultrices est congue vel. Vivamus lectus tortor, posuere ut fringilla ac, sollicitudin quis mauris. Duis et accumsan ipsum, at hendrerit lorem.</p><p>In consectetur scelerisque tellus, eget sollicitudin risus imperdiet in. Phasellus quis elit consequat, porttitor metus in, interdum ipsum. Aenean sit amet commodo est. Etiam est turpis, congue bibendum vehicula non, mollis vel dui. Sed tincidunt lectus eget ligula volutpat, vitae ornare risus hendrerit. Aliquam scelerisque pellentesque iaculis. Quisque ac arcu quis risus molestie tempus ac eget ante. Duis in est eu sapien mattis euismod nec a quam. Pellentesque vitae erat venenatis, convallis ipsum eget, convallis erat. Curabitur in ante eget ipsum elementum varius pulvinar vel turpis. Nullam pulvinar nisl at ligula viverra laoreet ac eu nulla.&nbsp;</p>"


def poblar(cantidad, funciones):
    """
    int(cantidad), list(funciones)
    """
    for f in funciones:
        print f, cantidad
        f(cantidad)

def crear_hilos_conductores(cantidad):
    """
    Crea int(cantidad) de hilos conductores.
    """
    for n in range(cantidad):
        HiloConductor(nombre="Hilo {0} nombre largo".format(str(n)), nombre_corto="Hilo {0}".format(str(n))).save()

def crear_topicos_generativos(cantidad):
    """
    Crea int(cantidad) de tópicos generativos.
    """
    for n in range(cantidad):
        TopicoGenerativo(nombre="Topico generativo {0} nombre largo".format(str(n)), nombre_corto="Topico generativo {0}".format(str(n))).save()

def crear_metas_de_comprension(cantidad):
    """Crea int(cantidad) de tópicos generativos.
    """
    for n in range(cantidad):
        MetaDeComprension(nombre="Meta de comprensión {0} nombre largo".format(str(n)), nombre_corto="Meta de comprensión {0}".format(str(n))).save()

def crear_tags(cantidad):
    """Crea int(cantidad) de tags.
    """
    for n in range(cantidad):
        Tag(name="Tag {0}-{1}".format(str(n), datetime.datetime.now().strftime("%d%m%d%H%M%S%f")), slug="Tag {0}-{1}".format(str(n), datetime.datetime.now().strftime("%d%m%d%H%M%S%f"))).save()

def crear_recursos(cantidad):
    """Crea int(cantidad) de Recursos.
    Requiere que exista un usuario de tipo django.contrib.auth.models.User y el manager de django-taggit
    """
    for n in range(cantidad):
        rec=Recurso(
            nombre="Nombre largo del recurso {0}".format(str(n)),
            nombre_corto="recurso-{0}-{1}".format(str(n),datetime.datetime.now().strftime("%d%m%d%H%M%S%f")),
            cuerpo=LOREM_IPSUM,
            tipo='MLT',
            url="ftp://miadjunto.ftp.yo.com",
            imagen_destacada='recurso_adjunto/5-8_color.png')
        rec.save()
        RecursosAutores(recurso=rec, autor=USUARIO).save()
        rec.tags.add("Tag {0}-{1}".format(str(n), datetime.datetime.now().strftime("%d%m%d%H%M%S%f")))
        
def crear_desempenos_de_comprension(cantidad):
    """Crear int(cantidad) de desempeños de comprensión.
    """
    for n in range(cantidad):
        des=DesempenoDeComprension(
            nombre="Desempeño {0}".format(str(n)),
            nombre_corto="Desempeno-{0}".format(datetime.datetime.now().strftime("%d%m%d%H%M%S%f")),
            fecha_publicacion=datetime.datetime.now(),
            fecha_actualizacion=datetime.datetime.now(),
            cuerpo=LOREM_IPSUM,
            notas_profesor=LOREM_IPSUM,
            duracion=60,
            imagen_destacada='recurso_adjunto/5-8_color.png'
            )
        des.save()
        rec=Recurso.objects.get(pk=1)
        DesempenosDeComprensionAutores(desempeno_de_comprension=des, autor=USUARIO).save()     
        DesempenosDeComprensionRecursos(desempeno_de_comprension=des, recurso=rec).save()
        
def crear_cursos(cantidad):
    for n in range(cantidad):
        c=Curso(
            codigo="CTEST-{0}".format(str(n)),
            nombre="Curso llamado {0}".format(datetime.datetime.now().strftime("%d%m%d%H%M%S%f")),
            acceso='AB-L',
            fecha_inicio=datetime.datetime.now(),
            cupos=10,
        )
        c.save()
        CursosProfesores(curso=c, profesor=USUARIO).save()
        hilo=HiloConductor.objects.all()[0]
        CursosHilosConductores(curso=c, hilo_conductor=hilo).save()
        topico=TopicoGenerativo.objects.all()[0]
        CursosTopicosGenerativos(curso=c, topico_generativo=topico).save()
        meta=MetaDeComprension.objects.all()[0]
        CursosMetasDeComprension(curso=c, meta_de_comprension=meta).save()
        desempeno=DesempenoDeComprension.objects.all()[0]
        CursosDesempenosDeComprension(curso=c, desempeno_de_comprension=desempeno, orden=1).save()
        c.tags.add("Tag {0}-{1}".format(str(n), datetime.datetime.now().strftime("%d%m%d%H%M%S%f")))
        

FUNCIONES = [crear_hilos_conductores, crear_topicos_generativos, crear_metas_de_comprension, crear_recursos, crear_tags, crear_desempenos_de_comprension, crear_cursos]

poblar(CANTIDAD,FUNCIONES)