
from django.urls import path
from libros.views import index, lista_libros, libros_create, lista_autores, LibroDetail
#from config import views

app_name = "libros"
urlpatterns = [
    path("", index, name="index"),
    path("libros/lista",lista_libros, name="lista_libros"),
    path("libros/create",libros_create,name="libros_create"),
    path("libros/autores",lista_autores,name="lista_autores"),
    path("libros/detail/<int:pk>",LibroDetail.as_view(),name="libro_detail") 
]