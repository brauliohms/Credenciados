from django.db import models
from unidecode import unidecode


# classe responsavel por criar essa tabela no banco de dados
class Credenciado(models.Model):
    ESTADOS = [
        ("AC", "AC"),
        ("AL", "AL"),
        ("AP", "AP"),
        ("AM", "AM"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("DF", "DF"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO"),
    ]

    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telefone = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=60, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True, choices=ESTADOS)
    servicos = models.TextField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    # função para realizar alguma ação ao salvar no banco
    def save(self, *args, **kwargs):
        # do campo nome, remove acentos (unidecode), remove espacos em branco (strip)
        # e deixa tudo em maiusculas (upper)
        self.nome = unidecode(self.nome).strip().upper()
        # O if é para acontecer se somente aquele campo houver dados
        if self.email:
            self.email = self.email.strip().lower()
        if self.servicos:
            self.servicos = unidecode(self.servicos).strip().upper()
        super().save(*args, **kwargs)
