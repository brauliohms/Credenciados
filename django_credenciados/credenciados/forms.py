from django import forms

from .models import Credenciado


class FormCredenciado(forms.ModelForm):
    class Meta:
        model = Credenciado
        fields = "__all__"
        widgets = {
            "nome": forms.TextInput(attrs={"size": "45"}),
            "cnpj": forms.TextInput(attrs={"size": "14", "oninput": "formatarCNPJ(this)"}),
            "email": forms.TextInput(attrs={"size": "35"}),
            "telefone": forms.TextInput(attrs={"size": "35"}),
            "endereco": forms.TextInput(attrs={"size": "55"}),
            "cidade": forms.TextInput(attrs={"size": "35"}),
        }
