"""MiProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MiProyecto.views import bienvenida, bienvenidaRojo, categoriaEdad, \
    obtenerMomentoActual, contenidoHTML, miPrimeraPlantilla, plantilla_parametros, plantillaCargado, plantillaHija1, plantillaHija2, plantillaShortcut

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/', bienvenida),
    path('bienvenida123/', bienvenidaRojo),
    path('categoriaedad/<int:edad>', categoriaEdad),
    path('hora/', obtenerMomentoActual),
    path('contenidohtml/<nombre>/<int:edad>', contenidoHTML),
    path('template/', miPrimeraPlantilla),
    path('plantilla_parametros/', plantilla_parametros),
    path('plantilla_cargador', plantillaCargado),
    path('plantilla_shortcut/', plantillaShortcut),
    path('plantilla_hija1/', plantillaHija1),
    path('plantilla_hija2/', plantillaHija2)
]
