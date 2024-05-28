
from django.urls import path
from libros.views import index, lista_libros, libros_create, lista_autores, LibroDetail, LibroUpdate, LibroDelete, AutorDetail
#from config import views

app_name = "libros"
urlpatterns = [
    path("", index, name="index"),
    path("libros/lista",lista_libros, name="lista_libros"),
    path("libros/create",libros_create,name="libros_create"),
    path("libros/autores",lista_autores,name="lista_autores"),
    path("libros/detail/<int:pk>",LibroDetail.as_view(),name="libro_detail") ,
    path("libros/update/<int:pk>",LibroUpdate.as_view(),name="libro_update"),
    path("libros/delete/<int:pk>",LibroDelete.as_view(),name="libro_delete"),
    path("libros/libroporautor_detail/<int:pk>",AutorDetail.as_view(),name="libroporautor_detail")
]