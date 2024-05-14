
from django.urls import path
from libros.views import index, lista_libros, libros_create
#from config import views

app_name = "libros"
urlpatterns = [
    path("", index, name="index"),
    path("libros/lista",lista_libros, name="lista_libros"),
    path("libros/create",libros_create,name="libros_create"), # type: ignore
]