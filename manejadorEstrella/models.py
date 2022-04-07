from django.db import models

# Create your models here.
class estrella(models.Model):
    nombre = models.CharField(max_length=40, null = True)
    direccion = models.CharField(max_length=20, null = True)
    email = models.EmailField(null = True)
    tfo = models.CharField(max_length=20, null = True)
    universidad = models.CharField(max_length=40, null = True)
    link = models.URLField(null = True)
    link = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.1=" + str(direccion) + "&wp.2=" + str(direccion) + ",&key=Am3rc5_fSLkVOUrt2RNLAWIqdNgx3j2kxwyK-5mUd5gf5g59XJ8MMXUhJbcSZZvZ"

    @classmethod
    def create(cls, nombre, direccion, email, tfo, universidad, link):
        estre = cls(nombre=nombre, direccion = direccion, 
                email = email, tfo = tfo, universidad = universidad,
                link = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.1={}&wp.2={},&key=Am3rc5_fSLkVOUrt2RNLAWIqdNgx3j2kxwyK-5mUd5gf5g59XJ8MMXUhJbcSZZvZ".format(str(direccion), str(universidad)))
        return estre


    #link = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.1={}&wp.2={},&key=Am3rc5_fSLkVOUrt2RNLAWIqdNgx3j2kxwyK-5mUd5gf5g59XJ8MMXUhJbcSZZvZ".format(str(direccion), str(universidad))
  
    def  __str__(self):
        x = self.nombre + "\n" + self.direccion + "\n" + self.email + "\n" + self.tfo + "\n" + self.universidad + "\n" + self.link
        return(x)