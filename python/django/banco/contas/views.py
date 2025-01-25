from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ContaCorrente
from .forms import ContaForm
from django.db import models
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.timezone import now



def index(request):
    """Página inicial que lista todas as contas cadastradas com links para ações."""
    contas = ContaCorrente.objects.all()  # Recupera todas as contas
    return render(request, 'contas/index.html', {'contas': contas})

def detalhes(request, conta_id):
    # Busca a conta pelo ID
    conta = get_object_or_404(ContaCorrente, pk=conta_id)

    # Renderiza os detalhes da conta
    return render(request, 'contas/detalhes_conta_corrente.html', {'conta': conta})

def criar_conta(request):
    if request.method == 'POST':
        form = ContaForm(request.POST)
        if form.is_valid():
            conta = form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect('exibir_conta', numero_conta=conta.numero_conta)
        else:
            messages.error(request, "Erro ao criar a conta. Verifique os dados.")
    else:
        form = ContaForm()
    return render(request, 'contas/criar_conta.html', {'form': form})


def depositar(request, conta_id):
    conta = get_object_or_404(ContaCorrente, pk=conta_id)

    if request.method == "POST":
        valor = float(request.POST.get("valor"))
        conta.saldo += valor
        conta.save()
        
        # Registra no histórico
        conta.historico.create(operacao="Depósito", valor=valor, saldo=conta.saldo)
        return redirect('detalhes', conta_id=conta.id)

    return render(request, 'contas/depositar.html', {'conta': conta})

def sacar(request, conta_id):
    conta = get_object_or_404(ContaCorrente, pk=conta_id)

    if request.method == "POST":
        valor = float(request.POST.get("valor"))
        if conta.saldo - valor >= conta.limite_negativo:
            conta.saldo -= valor
            conta.save()
            conta.historico.create(operacao="Saque", valor=-valor, saldo=conta.saldo)
        else:
            return render(request, 'contas/sacar.html', {'conta': conta, 'erro': "Saldo insuficiente."})

        return redirect('detalhes', conta_id=conta.id)

    return render(request, 'contas/sacar.html', {'conta': conta})

def transferir(request, conta_id):
    conta_origem = get_object_or_404(ContaCorrente, pk=conta_id)
    contas = ContaCorrente.objects.exclude(pk=conta_id)

    if request.method == "POST":
        valor = float(request.POST.get("valor"))
        conta_destino_id = request.POST.get("conta_destino")
        conta_destino = get_object_or_404(ContaCorrente, pk=conta_destino_id)

        if conta_origem.saldo - valor >= conta_origem.limite_negativo:
            conta_origem.saldo -= valor
            conta_destino.saldo += valor
            conta_origem.save()
            conta_destino.save()

            conta_origem.historico.create(operacao="Transferência Enviada", valor=-valor, saldo=conta_origem.saldo)
            conta_destino.historico.create(operacao="Transferência Recebida", valor=valor, saldo=conta_destino.saldo)

            return redirect('detalhes', conta_id=conta_origem.id)
        else:
            return render(request, 'contas/transferir.html', {'conta': conta_origem, 'contas': contas, 'erro': "Saldo insuficiente."})

    return render(request, 'contas/transferir.html', {'conta': conta_origem, 'contas': contas})


def historico(request, conta_id):
    # Busca a conta
    conta = get_object_or_404(ContaCorrente, pk=conta_id)
    # Busca todas as operações associadas a essa conta
    historico = conta.historico.all()

    # Renderiza o template com os dados
    return render(request, 'contas/historico.html', {'conta': conta, 'historico': historico})