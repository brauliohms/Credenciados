from django.test import TestCase

from ..models import Credenciado


class CredenciadoTestCase(TestCase):
    # Inicializar um banco novo com o seguinte usuario para testes de criação
    def setUp(self):
        Credenciado.objects.create(
            nome="Hóspital FAB",
            email="Hospital@Fab.mil.br",
            telefone="(21)3563-1122",
            servicos="Tomografia, RX-Tórax, nêurocirurgia",
        )

    # Testar se o credenciado esta sendo criado no banco apenas e nome upper sem acentos
    def test_credenciado_criado_no_banco_nome_upper(self):
        credenciado = Credenciado.objects.get(nome="HOSPITAL FAB")
        self.assertTrue(credenciado)

    # Testar se o credenciado esta sendo criado no banco apenas e email lower
    def test_credenciado_criado_no_banco_email_lower(self):
        credenciado = Credenciado.objects.get(email="hospital@fab.mil.br")
        self.assertTrue(credenciado)

    # Testar se o credenciado esta sendo criado e esta colocando nome no __str__
    def test_credenciado_str(self):
        credenciado = Credenciado.objects.get(email="hospital@fab.mil.br")
        self.assertEqual(credenciado.__str__(), "HOSPITAL FAB")

    # Testar se o servico ficou como UPPER e sem acentos caso usuario digitar errado
    def test_credenciado_criado_servico_upper(self):
        credenciado = Credenciado.objects.get(email="hospital@fab.mil.br")
        self.assertEqual(credenciado.servicos, "TOMOGRAFIA, RX-TORAX, NEUROCIRURGIA")
