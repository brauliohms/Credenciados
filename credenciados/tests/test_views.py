from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from usuarios.models import Usuario

from ..models import Credenciado


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_index = reverse("index")
        self.url_busca_nome = reverse("buscar_nomes")
        self.url_busca_servico = reverse("buscar_servicos")
        self.url_add_credenciado = reverse("add_credenciado")

        self.credenciado1 = Credenciado.objects.create(
            nome="Hospital FAB", cnpj="11.222.333/0001-44", email="hospital@fab.mil.br"
        )

        # Cria um usuário para fins de autenticação nos testes
        self.username = "testuser"
        self.password = "testpassword"
        self.cpf = "111.222.333-44"
        self.user = Usuario.objects.create_user(username=self.username, password=self.password)

    def test_status_code_add_credenciado_autenticado_200(self):
        # Autentica o usuário
        self.client.login(username=self.username, password=self.password)
        # Faz a solicitação GET para a URL após autenticação
        response = self.client.get(self.url_add_credenciado)
        # Verifica o status code esperado
        self.assertEqual(response.status_code, 200)

    # Teste para verificar se o arquivo template html que esta renderizando está correto
    def test_template_add_credenciado_autenticado(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url_add_credenciado)
        self.assertTemplateUsed(response, "credenciados/add_credenciado.html")

    # Teste para ver se o redirecionamento de Login Requerido da view esta funcionando
    def test_status_code_add_usuario_nao_autenticado_302(self):
        response = self.client.get(self.url_add_credenciado)
        self.assertEqual(response.status_code, 302)

    # Teste para verificar se o arquivo template html que esta renderizando está correto
    def test_template_add_credenciado_nao_autenticado(self):
        response = self.client.get(self.url_add_credenciado)
        self.assertTemplateNotUsed(response, "credenciados/add_credenciado.html")

    # Teste para ver se o parametro de busca via GET da view esta funcionando
    def test_status_code_busca_nome_200(self):
        response = self.client.get(f"{self.url_busca_nome}?q=santa")
        self.assertEqual(response.status_code, 200)

    # Teste para verificar se o arquivo template html que esta renderizando está correto
    def test_template_busca_nome(self):
        response = self.client.get(f"{self.url_busca_nome}?q=santa")
        self.assertTemplateUsed(response, "credenciados/busca_nomes.html")

    # Teste para ver se o parametro de busca via GET da view esta funcionando
    def test_status_code_busca_servico_200(self):
        response = self.client.get(f"{self.url_busca_servico}?q=tomografia")
        self.assertEqual(response.status_code, 200)

    # Teste para verificar se o arquivo template html que esta renderizando está correto
    def test_template_busca_servico(self):
        response = self.client.get(f"{self.url_busca_servico}?q=tomografia")
        self.assertTemplateUsed(response, "credenciados/busca_servicos.html")

    # Teste para verificar se o arquivo template html que esta renderizando está correto
    def test_template_used_index(self):
        response = self.client.get(self.url_index)
        self.assertTemplateUsed(response, "credenciados/index.html")
