from django.contrib.auth.models import AbstractUser
from django.db import models


# classe responsavel pelo tabela Usuario no banco de dados
# herda de AbstractUser para sobrescrever a classe User padrao Django
class Usuario(AbstractUser):
    PATENTES = (
        ("TB", "TB"),
        ("MB", "MB"),
        ("BG", "BG"),
        ("CL", "CL"),
        ("TC", "TC"),
        ("MJ", "MJ"),
        ("CP", "CP"),
        ("1T", "1T"),
        ("2T", "2T"),
        ("SO", "SO"),
        ("1S", "1S"),
        ("2S", "2S"),
        ("3S", "3S"),
        ("S1", "S1"),
        ("S2", "S2"),
    )
    posto_graduacao = models.CharField(max_length=2, blank=True, null=True, choices=PATENTES)
    nome_guerra = models.CharField(max_length=30, blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True)
    saram = models.CharField(max_length=10, blank=True, null=True)

    # metodo que retorna o nome que represena um objeto instanciado dessa classe
    # ou seja, como um registro vai ser representado para exibicao curta
    def __str__(self):
        return f"{self.posto_graduacao} {self.nome_guerra}"

    # metodo para realizar alguma coisa na hora que for salvar no banco
    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.strip().title()
        if self.last_name:
            self.last_name = self.last_name.strip().title()
        self.username = self.username.strip().lower()
        if self.email:
            self.email = self.email.strip().lower()
        if self.nome_guerra:
            self.nome_guerra = self.nome_guerra.strip().upper()
        super().save(*args, **kwargs)
