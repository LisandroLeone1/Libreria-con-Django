
from django.urls import path
from ventas.views import VentasList, VentasCreate, VentasDetail, VentasUpdate, VentasDelete
#from config import views

app_name = "ventas"
urlpatterns = [
    path("ventas/lista",VentasList.as_view(),name="ventas_lista"),
    path("ventas/create", VentasCreate.as_view(), name="ventas_create"),
    path("ventas/detail/<int:pk>",VentasDetail.as_view(),name="ventas_detail"),
    path("ventas/update/<int:pk>",VentasUpdate.as_view(),name="ventas_update"),
    path("ventas/delete/<int:pk>",VentasDelete.as_view(),name="ventas_delete")
]