from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ContaCorrente
from .forms import ContaForm
from django.core.paginator import Paginator
from django.shortcuts import render


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
    conta = get_object_or_404(ContaCorrente, id=conta_id)
    # Lógica para depósito
    return render(request, 'contas/depositar.html', {'conta': conta})

def sacar(request, conta_id):
    conta = get_object_or_404(ContaCorrente, id=conta_id)
    # Lógica para saque
    return render(request, 'contas/sacar.html', {'conta': conta})

def transferir(request, conta_id):
    conta = get_object_or_404(ContaCorrente, id=conta_id)
    # Lógica para transferência
    return render(request, 'contas/transferir.html', {'conta': conta})

def historico(request, conta_id):
    conta = get_object_or_404(ContaCorrente, id=conta_id)
    historico = conta.historico_set.all()
    return render(request, 'contas/historico.html', {'conta': conta, 'historico': historico})