from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import FormUsuario
from .models import Usuario


@login_required
def edit_usuario(request):
    usuario = request.user
    if request.method == "GET":
        form = FormUsuario(instance=usuario)
        return render(request, "usuarios/profile.html", {"form": form})

    elif request.method == "POST":
        form = FormUsuario(request.POST, instance=usuario)
        try:
            form.save()
            messages.success(
                request,
                f"Usuário {usuario.posto_graduacao} \
                             {usuario.nome_guerra} atualizado com sucesso",
            )
            return redirect("index")
        except:
            messages.error(
                request,
                "Erro interno no banco de dados ao salvar \
                           as alterações",
            )
            return redirect("edit_usuario")


@login_required
def sair(request):
    usuario = request.user
    auth.logout(request)
    messages.success(request, f"{usuario} saiu com sucesso")
    return redirect("index")
