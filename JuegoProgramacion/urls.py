"""JuegoProgramacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from apps.alumnos.views import *
from apps.profesores.views import *
urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^jugar/(?P<matricula>\d+)/(?P<idjuego>\d+)/', Jugar, name="Jugar"),
    url(r'^registraralumno/(?P<matricula>\d+)/', RegistrarAlu, name="RegistrarAlu"),
    url(r'^registrarprofesor/(?P<matricula>\d+)/', RegistrarProf, name="RegistrarProf"),
    url(r'^registrargrupo/(?P<matricula>\d+)/', RegistrarGr, name="RegistrarGr"),
    url(r'^registrarjuego/(?P<matricula>\d+)/', RegistrarJu, name="RegistrarJuego"),
    url(r'^lista_profesores/(?P<matricula>\d+)/', ProfesoresList, name="ProfesoresList"),
    url(r'^editarprofesor/(?P<matricula>\d+)/(?P<matricula2>\d+)/', ProfesoresEdit, name="ProfesoresEdit"),
    url(r'^lista_alumnos/(?P<matricula>\d+)/', AlumnosList, name="AlumnosList"),
    url(r'^editar/(?P<matricula>\d+)/(?P<matricula2>\d+)/', AlumnosEdit, name="AlumnosEdit"),
    url(r'^$', LoginAlumnos, name="LoginAlumnos"),
    url(r'^lista_juegos/(?P<matricula>\d+)/', JuegosList, name="JuegosList"),
    url(r'^editar_juego/(?P<matricula>\d+)/(?P<id>\d+)/', JuegosEdit, name="JuegosEdit"),
    url(r'^profesores/', LoginProfesores, name="LoginProfesores"),
    url(r'^Administracion/(?P<matricula>\d+)/', IndexProf, name="IndexProf"),
    url(r'^index/(?P<matricula>\d+)/', index, name="index"),
    url(r'^test/', test, name="test"),
    url(r'^sg/(?P<matricula>\d+)/(?P<idjuego>\d+)/(?P<horas>\d+)/(?P<minutos>\d+)/(?P<segundos>\d+)/(?P<CantidadInstrucciones>\d+)/', sg, name="sg"),
	url(r'^Traductor/', Traductor, name="Traductor"),
]
