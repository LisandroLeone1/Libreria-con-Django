from django.shortcuts import render
from autores.models import Autores
def index(request):
    return render(request,"autores/index.html")

def lista_autores(request):
    consulta = Autores.objects.all()
    contexto = {"autor": consulta}
    return render(request,"autores/lista_autores.html",contexto)

