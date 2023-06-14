from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario


@admin.register(Usuario)
class CustomUserAdmin(UserAdmin):
    model = Usuario
    list_display = ("posto_graduacao", "nome_guerra", "username", "email", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (
            "Dados do Militar",
            {
                "fields": (
                    "posto_graduacao",
                    "nome_guerra",
                    "cpf",
                    "saram",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Dados do Militar",
            {
                "fields": (
                    "posto_graduacao",
                    "nome_guerra",
                    "email",
                    "cpf",
                    "saram",
                )
            },
        ),
    )
