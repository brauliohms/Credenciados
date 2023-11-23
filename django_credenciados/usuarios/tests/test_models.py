from django.db.utils import IntegrityError
from django.test import TestCase

from ..models import Usuario


class UsuarioTestCase(TestCase):
    # Inicializar um banco novo com o seguinte usuario para testes de criação
    def setUp(self):
        Usuario.objects.create(
            username="militarmfp",
            email="militarmfp@fab.mil.br",
            first_name="Militar",
            last_name="Fab Padrão",
            posto_graduacao="2T",
            nome_guerra="militar fab",
            cpf="111.222.333-45",
            saram="1001232",
        )

    # Esse teste e o próximo são vão passar se der erro na criação do usuario
    def test_nao_pode_criar_usuario_com_username_duplicado(self):
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(
                username="militarmfp",
                email="militarmfp2@fab.mil.br",
                first_name="Militar2",
                last_name="Fab Padrão",
                posto_graduacao="2T",
                nome_guerra="militar2 fab",
                cpf="222.333.444-55",
                saram="1001233",
            )

    def test_nao_pode_criar_usuario_com_cpf_duplicado(self):
        with self.assertRaises(IntegrityError):
            Usuario.objects.create(
                username="militarmfp3",
                email="militarmfp3@fab.mil.br",
                first_name="Militar3",
                last_name="Fab Padrão",
                posto_graduacao="2T",
                nome_guerra="militar3 fab",
                cpf="111.222.333-45",
                saram="1001234",
            )

    # Testar se o usuário esta sendo criado no banco apenas
    def test_usuario_criado_no_banco(self):
        usuario = Usuario.objects.get(username="militarmfp")
        self.assertTrue(usuario)

    # Testar se o usuário esta sendo criado e esta colocando nome_guerra em UPPER
    def test_usuario_str(self):
        usuario = Usuario.objects.get(username="militarmfp")
        self.assertEqual(usuario.__str__(), "2T MILITAR FAB")

    # Testar se o nome_guerra não ficou como foi digitado (lower)
    def test_usuario_criado_nome_guerra_upper(self):
        usuario = Usuario.objects.get(username="militarmfp")
        self.assertNotEqual(usuario.nome_guerra, "militar fab")
