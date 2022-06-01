from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=15)
    telefono = models.CharField(max_length=15)
    correo = models.CharField(max_length=50)

class DeclaracionGanancia(models.Model):
    ganancia = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    dinero = models.IntegerField()

class DeclaracionPerdida(models.Model):
    perdida = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    dinero = models.IntegerField()