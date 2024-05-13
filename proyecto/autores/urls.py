from django.urls import path
from autores.views import index, lista_autores
#from config import views

app_name = "autores"

urlpatterns = [
    path("", index, name="index"),
    path("autores/lista",lista_autores, name="lista_autores"),
]