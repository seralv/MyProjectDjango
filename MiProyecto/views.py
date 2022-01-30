from datetime import datetime
from django.template import Template, Context

from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse("Welcome here with Django")

def bienvenidaRojo(request):
    return HttpResponse("<p style='color: red;'>Welcome in red too")

def categoriaEdad(request, edad):
    if edad >= 18:
        if edad >= 60:
            categoria = "Tercera edad"
        else:
            categoria = "Adultez"
    else:
        if edad < 10:
            categoria = "Infancia"
        else:
            categoria = "Adolescencia"

    resultado = "<h1>Categoria de la edad: %s</h1>" % categoria
    return HttpResponse(resultado)

def obtenerMomentoActual(request):
    respuesta = "<h1>Momento actual: {0}</h1".format(datetime.now().strftime("%A %d/%m/%Y %H:%M:%S"))
    return HttpResponse(respuesta)

def contenidoHTML(request, nombre, edad):
    contenido = """
    <html>
    <body>
    <p>Nombre: %s / Edad: %s</p>
    </body>
    </html>
    """%(nombre.title(), edad)
    return HttpResponse(contenido)

def miPrimeraPlantilla(request):
    plantillaExterna = open("/home/sergio/Documentos/Django/MiProyecto/MiProyecto/templates/miPrimeraPlantilla.html")
    template = Template(plantillaExterna.read())
    plantillaExterna.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)