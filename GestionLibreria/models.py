from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=50)
    editorial = models.CharField(max_length=30)
    fecha_publicacion = models.DateTimeField(default=timezone.now)

class Revista(models.Model):
    empresa = models.CharField(max_length=30)
    tipo_lanzamiento = models.CharField(max_length=30)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    
class Empleado(models.Model):
    dni = models.CharField(max_length=9)
    nombre = models.CharField(max_length=30)
    edad = models.CharField(max_length=2)