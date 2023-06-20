from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from ..models import Usuario


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("edit_usuario")

        # Cria um usuário para fins de autenticação nos testes
        self.username = "testuser"
        self.password = "testpassword"
        self.cpf = "111.222.333-44"
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)

    def test_status_code_edit_usuario_autenticado_200(self):
        # Autentica o usuário
        self.client.login(username=self.username, password=self.password)
        # Faz a solicitação GET para a URL após autenticação
        response = self.client.get(self.url)
        # Verifica o status code esperado
        self.assertEqual(response.status_code, 200)

    def test_template_edit_usuario_autenticado(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "usuarios/profile.html")

    # Teste para ver se o redirecionamento de Login Requerido da view esta funcionando
    def test_status_code_edit_usuario_nao_autenticado_302(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_template_edit_usuario_nao_autenticado(self):
        response = self.client.get(self.url)
        self.assertTemplateNotUsed(response, "usuarios/profile.html")
