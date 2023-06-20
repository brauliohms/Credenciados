from django.http import HttpRequest
from django.test import TestCase

from ..forms import FormCredenciado


class FormTestCase(TestCase):
    def setUp(self):
        self.form = FormCredenciado()

    # Testar se todos os campos estão no formulário com exato nome
    def test_campos_form(self):
        self.assertIn("nome", self.form.fields)
        self.assertIn("cnpj", self.form.fields)
        self.assertIn("email", self.form.fields)
        self.assertIn("telefone", self.form.fields)
        self.assertIn("endereco", self.form.fields)
        self.assertIn("cidade", self.form.fields)
        self.assertIn("uf", self.form.fields)
        self.assertIn("servicos", self.form.fields)
        self.assertIn("observacao", self.form.fields)

    # Testar se todos os campos do formulário estao recebendo os dados corretamente
    def test_form_is_valid(self):
        request = HttpRequest()
        request.POST = {
            "nome": "Hospital FAB",
            "cnpj": "11.222.333/0001-44",
            "email": "hospital@fab.mil.br",
            "telefone": "(21) 3566-2211",
            "endereco": "Avenida da Saude, 32",
            "cidade": "Rio de Janeiro",
            "uf": "RJ",
            "servicos": "TOMOGRAFIA, RX-TORAX, NEUROCIRURGIA",
            "observacao": "sem filas",
        }
        form = FormCredenciado(request.POST)
        self.assertTrue(form.is_valid())
