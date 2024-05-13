from django.db import models
from autores.models import Autores

class Editorial(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    nombre = models.CharField(max_length=100,unique=True)
    año = models.DateField
    editorial = models.ForeignKey(Editorial,on_delete=models.SET_NULL, null=True,blank=True)
    autor = models.ForeignKey(Autores,on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.año}"
    