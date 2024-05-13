from django.shortcuts import render
from libros.models import Libro

def index(request):
    return render(request,"libros/index.html")

def lista_libros(request):
    consulta = Libro.objects.all()
    contexto = {"libros": consulta}
    return render(request,"libros/lista_libros.html",contexto)