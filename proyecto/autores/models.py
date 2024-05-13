from django.db import models
#from libros.models import Libro

class Autores(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100,null=True,blank=True)
    naciomiento = models.DateField(null=True,blank=True)
    #libros = models.ManyToManyField(Libro)


    def __str__(self):
        return f"{self.nombre}. Nacionalidad: {self.nacionalidad}. Nacimiento: {self.naciomiento}"
