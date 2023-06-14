from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def __str__(self):
        return f"{self.posto_graduacao} {self.nome_guerra}"

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.strip().title()
        self.last_name = self.last_name.strip().title()
        self.username = self.username.strip().lower()
        self.email = self.email.strip().lower()
        self.nome_guerra = self.nome_guerra.strip().upper()
        super().save(*args, **kwargs)
