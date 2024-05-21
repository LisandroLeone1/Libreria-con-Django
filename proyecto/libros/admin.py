from django.contrib import admin

from .models import Editorial, Libro, Autores, LibroPorAutor

admin.site.register(Editorial)
admin.site.register(Libro)
admin.site.register(Autores)
admin.site.register(LibroPorAutor)
