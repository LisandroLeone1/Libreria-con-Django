from django.http import HttpResponse
from django.shortcuts import render

def saludo(request):
    return HttpResponse("Mi proyecto")

def nombre(request, nombre: str, apellido:str):
   nombre = nombre.capitalize()
   apellido = apellido.capitalize()
   return HttpResponse (F"Mi nombre es {nombre} {apellido}")

def probando(request):
    datos = {"Saludo": "Bienvenido", "Autor": "Lisandro"}
    return render(request,"templates.html",datos)

def tupla(request):
    tupla = (1,2,3,4,5)
    return render(request,"tupla.html",{"tupla":tupla})

def lista(request):
    lista = ["pera","naranja","manzana","mandaria"]
    return render(request,"lista.html",{"lista":lista})