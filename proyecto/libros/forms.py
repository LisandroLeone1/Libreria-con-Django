from django import forms
from . import models

class LibroForms(forms.ModelForm):
    class Meta:
        model = models.Libro
        fields = "__all__"