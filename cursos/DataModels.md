Recurso
#Atributos b‡sicos y obligatorios
    autor=settings.AUTH_USER_MODEL,
    nombre=CharField
    nombre_corto=SlugField
    html=RichTextField
    tipo=CharField (choices)
    #Atributos opcionales
    adjunto=FileField
    url=URLField
    #Metadatos opcionales
    imagen_destacada=ImageField
    tags=TaggableManager()
HiloConductor
TopicoGenerativo
MetaDeComprension
DesempenoDeComprension
Curso
RecursosAutores
DesempenosDeComprensionAutores
DesempenosDeComprensionRecursos
CursosProfesores
CursosHilosConductores
CursosTopicosGenerativos
CursosMetasDeComprension
CursosDesempenosDeComprension
CursosInscritos

