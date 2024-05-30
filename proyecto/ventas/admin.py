from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Venta"


class VentaAdmin(admin.ModelAdmin):
    list_display = (
        "vendedor",
        "libro",
        "cantidad",
        "precio_total",
        "fecha_venta",
    )
    list_display_links = ("libro",)
    search_fields = ("libro.nombre_libro", "vendedor")
    list_filter = ("vendedor",)
    date_hierarchy = "fecha_venta"


admin.site.register(models.Vendedor)
admin.site.register(models.Venta, VentaAdmin)