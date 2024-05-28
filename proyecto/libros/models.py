from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre
    
class Autores(models.Model):
    nombre_autor = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100,null=True,blank=True)
    nacimiento = models.DateField(null=True,blank=True)
    #libros = models.ManyToManyField(Libro)

    def __str__(self)-> str:
        return self.nombre_autor
    
class Libro(models.Model):
    nombre_libro = models.CharField(max_length=100,unique=True)
    año = models.DateField
    editorial = models.ForeignKey(Editorial,on_delete=models.SET_NULL, null=True,blank=True)
    autor = models.ForeignKey(Autores,on_delete=models.SET_NULL, null=True,blank=True)
    
    def __str__(self) -> str:
        return self.nombre_libro
    
class LibroPorAutor(models.Model):
    nombre = models.ForeignKey(Autores, on_delete=models.SET_NULL,null=True,blank=True)
    libros = models.ManyToManyField(Libro)

    def __str__(self):
        return self.nombre.nombre_autor

  
           