from django.shortcuts import render, redirect
from ventas.models import Vendedor, Venta
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.db.models.query import QuerySet
from ventas.forms import VentasForms


class VentasList(ListView):
    model = Venta
    context_object_name = "vendedores"
    template_name = "venta_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = Venta.objects.filter(vendedor__icontains = busqueda)
        return queryset
      

class VentasCreate(CreateView):
    model = Venta
    form_class = VentasForms
    success_url = reverse_lazy("venta:venta_list")


class VentasDetail(DetailView):
    model = Venta


class VentasUpdate(UpdateView):
    model = Venta
    form_class = VentasForms
    success_url = reverse_lazy("venta:venta_list")


class ProductoDelete(DeleteView):
    model = Venta
    success_url = reverse_lazy("venta:venta_list")
