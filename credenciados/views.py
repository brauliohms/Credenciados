from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import FormCredenciado
from .models import Credenciado


def index(request):
    # Obter todos os credenciados cadastrados e ordenar por nome
    credenciados = Credenciado.objects.all().order_by("nome")
    return render(request, "credenciados/index.html", {"credenciados": credenciados})


def buscar_nomes(request):
    query = request.GET.get("q")
    credenciados = Credenciado.objects.filter(nome__icontains=query)
    return render(
        request, "credenciados/busca_nomes.html", {"credenciados": credenciados, "query": query}
    )


def buscar_servicos(request):
    query = request.GET.get("q")
    credenciados = Credenciado.objects.filter(servicos__icontains=query)
    return render(
        request, "credenciados/busca_servicos.html", {"credenciados": credenciados, "query": query}
    )


def pdf_credenciado(request, pk):
    pass


@login_required  # somente usuario logado consegue executar essa função
def add_credenciado(request):
    # Se a requisição for GET, vai abrir um formulário em branco
    if request.method == "GET":
        form = FormCredenciado()
        return render(request, "credenciados/add_credenciado.html", {"form": form})

    # Se a requisicao for POST, os dados do formulario serao capturados para form
    elif request.method == "POST":
        form = FormCredenciado(request.POST)
        # Se todas as validaçoes dos campos estiverem Ok sera salvo no banco
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Credenciado adicionado com sucesso")
                return redirect("index")
            except:
                messages.error(
                    request,
                    "Não foi possivel adicionar o credenciado, erro interno \
                               no salvamento no banco de dados",
                )
                # através da função reverse, coloca-se o nome da view e ele constroi a URL
                return redirect("add_credenciado")
        else:
            messages.error(
                request,
                f"Não foi possível cadastrar, ocorreu erro no preenchimento do \
                formulário: {form.error}",
            )
            return redirect("add_credenciado")


@login_required
def edit_credenciado(request, pk):
    # Obter o credenciado do banco que corresponde ao parametro passado na url (pk)
    credenciado = get_object_or_404(Credenciado, pk=pk)
    if request.method == "GET":
        # instanciar um formulario preenchido com os dados do credenciado obtido
        form = FormCredenciado(instance=credenciado)
        return render(
            request, "credenciados/credenciado.html", {"form": form, "credenciado": credenciado}
        )
    elif request.method == "POST":
        form = FormCredenciado(request.POST, instance=credenciado)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Credenciado atualizado com sucesso")
                return redirect("index")
            except:
                messages.error(
                    request,
                    "Não foi possivel atualizar, erro interno \
                               no salvamento no banco de dados",
                )
                return redirect("credenciado")
        else:
            messages.error(
                request,
                f"Não foi possível atualizar, ocorreu erro no preenchimento do \
                formulário: {form.error}",
            )
            return redirect("credenciado")


@login_required
def del_credenciado(request, pk):
    credenciado = get_object_or_404(Credenciado, pk=pk)
    try:
        credenciado.delete()
        messages.success(request, "Credenciado excluído com sucesso")
        return redirect("index")
    except:
        messages.error(
            request,
            "Não foi possivel excluír o credenciado, erro interno \
                       no banco de dados",
        )
        return redirect("credenciado")
