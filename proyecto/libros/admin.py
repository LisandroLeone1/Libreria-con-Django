from django.contrib import admin
from .models import Editorial, Libro, Autores, LibroPorAutor

class LibroAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_libro",
        "autor",
        "editorial",
        "precio",
        "unidades"      )
    list_display_links = ("nombre_libro",)
    list_filter = ("autor","editorial")

admin.site.register(Editorial)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Autores)
admin.site.register(LibroPorAutor)
