from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from fpdf import FPDF

from .forms import FormCredenciado
from .models import Credenciado


def index(request):
    # Obter todos os credenciados cadastrados e ordenar por nome
    credenciados = Credenciado.objects.all().order_by("nome")
    return render(request, "credenciados/index.html", {"credenciados": credenciados})


def buscar_nomes(request):
    query = request.GET.get("q")
    credenciados = Credenciado.objects.filter(nome__icontains=query).order_by("nome")
    return render(
        request, "credenciados/busca_nomes.html", {"credenciados": credenciados, "query": query}
    )


def buscar_servicos(request):
    query = request.GET.get("q")
    credenciados = Credenciado.objects.filter(servicos__icontains=query).order_by("nome")
    return render(
        request, "credenciados/busca_servicos.html", {"credenciados": credenciados, "query": query}
    )


def pdf_credenciado(request, pk):
    credenciado = get_object_or_404(Credenciado, pk=pk)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", "B", 18)
    pdf.cell(80)
    pdf.cell(30, 10, "INFORMAÇÕES DO CREDENCIADO", align="C")
    pdf.set_line_width(0.5)
    pdf.line(x1=30, y1=20, x2=180, y2=20)
    pdf.ln(20)
    pdf.set_font("helvetica", size=14)
    pdf.write_html(
        f"""
            <h1><center>{credenciado.nome}</center></h1>
            <ul>
            <li><b>CNPJ:</b> {credenciado.cnpj}</li>
            <li><b>E-mail:</b> {credenciado.email}</li>
            <li><b>Telefone:</b> {credenciado.telefone}</li>
            <li><b>Endereço:</b> {credenciado.endereco}</li>
            <li><b>Cidade:</b> {credenciado.cidade} / {credenciado.uf}</li><br>
            <li><b>Serviços:</b><br>{credenciado.servicos}</li><br>
            <li><b>Observação:</b><br>{credenciado.observacao}</li>
            </ul>
    """
    )
    pdf.set_line_width(0.5)
    pdf.line(x1=30, y1=265, x2=180, y2=265)
    pdf.set_y(-30)
    pdf.set_font("helvetica", "I", 11)
    pdf.cell(
        0, 5, "FUNSA - GSAU-YS / Setor de Credenciamento", align="C", new_x="LMARGIN", new_y="NEXT"
    )
    pdf.cell(
        0,
        5,
        "Telefone: (19) 3565-7367 / E-mail: credenciamento.funsa.gsauys@fab.mil.br",
        align="C",
    )
    return HttpResponse(bytes(pdf.output()), content_type="application/pdf")


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
