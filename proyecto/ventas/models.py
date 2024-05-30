from django.contrib.auth.models import User
from django.db import models
from django.forms import ValidationError
from django.utils import timezone


# Create your models here.
class Vendedor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    celular = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="avatares", null=True, blank=True)
  
    def __str__(self) -> str:
        return self.usuario.username


class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True, blank=True)
    libro = models.ForeignKey("libros.Libro", on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        ordering = ("-fecha_venta",)

    def clean(self):
        if self.cantidad > self.libro.unidades:
            raise ValidationError("La cantidad vendida no puede ser mayor a la cantidad disponible")

    def save(self, *args, **kwargs):
        self.precio_total = self.libro.precio * self.cantidad
        super().save(*args, **kwargs)