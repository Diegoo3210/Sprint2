from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
import time, json
from manejadorEstrella.models import estrella

def saludo(request): #Primera vista
    return HttpResponse("Hola mi gente")

def sugerenciaTransporte(request): #Vista para la sugerencia de transporte

    direction = HttpResponseRedirect("http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.1=Seattle,WA&wp.2=Harvard-BelmontLandmarkDistrictSeattleWA,&key=Am3rc5_fSLkVOUrt2RNLAWIqdNgx3j2kxwyK-5mUd5gf5g59XJ8MMXUhJbcSZZvZ")
    ##Demora de un segundo que devuelva un JSON. 
    print("direccion: " + str(direction.url))
    y = "direccion: " + str(direction)

    print(request)

    return HttpResponse("Exito")

def obtenerUNLINK(request, id):
    estu = estrella.objects.get(pk=id)
    time.sleep(1) ##Se realiza la pregunta direcciones = "response(http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.1=Seattle,WA&wp.2=Harvard-BelmontLandmarkDistrictSeattleWA,&key=Am3rc5_fSLkVOUrt2RNLAWIqdNgx3j2kxwyK-5mUd5gf5g59XJ8MMXUhJbcSZZvZ)"
    direccion = json.load(direccion.json)
    return HttpResponse(direccion)