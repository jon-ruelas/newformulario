from django import forms

from newformulario.Models import Usuario


class FormularioUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
