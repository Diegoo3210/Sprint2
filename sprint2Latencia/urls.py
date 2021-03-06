"""sprint2Latencia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from urllib import request
from django.contrib import admin
from django.urls import path
from sprint2Latencia.views import saludo, sugerenciaTransporte, obtenerUNLINK
from sprint2Escalabilidad.views import index, uploadFile, inicio
from sprint2Latencia import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('sugerenciaTransporte/', sugerenciaTransporte),
    path('estrella/direccion/<id>', obtenerUNLINK),
    path('test/', index),
    path("uploadFile/", uploadFile),
    path("", inicio),
]
