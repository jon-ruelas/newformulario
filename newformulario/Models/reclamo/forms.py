from django import forms

from newformulario.Models import reclamo


class FormularioReclamo(forms.ModelForm):
    class Meta:
        model = reclamo
        fields = '__all__'
