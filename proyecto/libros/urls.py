
from django.urls import path
from libros.views import index, lista_libros
#from config import views

app_name = "libros"
urlpatterns = [
    path("", index, name="index"),
    path("libros/lista",lista_libros, name="lista_libros"),
    #path('saludo/', views.saludo),
    #path('nombre/<nombre>/<apellido>', views.nombre),
    #path('mi_html/', views.probando),
    #path('tupla/',views.tupla),
    #path('lista/',views.lista)
]