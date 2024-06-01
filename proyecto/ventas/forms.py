from django import forms
from . import models

class VentasForms(forms.ModelForm):
    class Meta:
        model = models.Venta
        fields = "__all__"