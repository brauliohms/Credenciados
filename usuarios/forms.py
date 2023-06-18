from django import forms

from .models import Usuario


class FormUsuario(forms.ModelForm):
    first_name = forms.CharField(max_length=50, label="Nome")
    last_name = forms.CharField(max_length=100, label="Sobrenome")
    posto_graduacao = forms.ChoiceField(choices=Usuario.PATENTES, label="Posto/Graduação")
    nome_guerra = forms.CharField(max_length=30, label="Nome de Guerra")

    class Meta:
        model = Usuario
        fields = [
            "first_name",
            "last_name",
            "posto_graduacao",
            "nome_guerra",
            "email",
            "cpf",
            "saram",
        ]
        widgets = {
            "email": forms.TextInput(attrs={"size": "25"}),
            "cpf": forms.TextInput(attrs={"size": "11", "oninput": "formatarCPF(this)"}),
            "saram": forms.TextInput(attrs={"size": "5"}),
        }
