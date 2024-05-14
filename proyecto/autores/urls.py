from django.urls import path
from autores.views import index
#from config import views

app_name = "autores"

urlpatterns = [
    path("", index, name="index"),
]