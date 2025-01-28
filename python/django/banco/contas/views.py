from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ContaCorrente, Historico
from .forms import ContaForm
from django.db import models
from django.core.paginator import Paginator
from django.utils.timezone import now
from decimal import Decimal
from django.core.exceptions import ValidationError

def index(request):
    """Página inicial que lista todas as contas cadastradas com links para ações."""
    contas = ContaCorrente.objects.all()  # Recupera todas as contas
    return render(request, 'contas/index.html', {'contas': contas})

def detalhes(request, conta_id):
    # Busca a conta pelo ID
    conta = get_object_or_404(ContaCorrente, pk=conta_id)

    # Renderiza os detalhes da conta
    return render(request, 'contas/detalhes_conta_corrente.html', {'conta': conta})

def depositar(request, conta_id):
    conta = ContaCorrente.objects.get(pk=conta_id)
    if request.method == 'POST':
        valor = Decimal(request.POST['valor'])
        conta.saldo += valor
        conta.save()

        Historico.objects.create(
            conta=conta,
            tipo="Depósito",
            valor=valor
        )
        return redirect('detalhes', conta_id=conta_id)
    return render(request, 'contas/depositar.html', {'conta': conta})

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


def sacar(request, conta_id):
    conta = get_object_or_404(ContaCorrente, pk=conta_id)

    if request.method == "POST":
        valor = Decimal(request.POST.get("valor"))
        if conta.saldo - valor < conta.limite_negativo:
            return render(request, 'contas/sacar.html', {
                'conta': conta,
                'erro': "Saldo insuficiente para o saque."
            })

        conta.saldo -= valor  # Subtrai do saldo da conta
        conta.save()

        # Registra a operação no histórico
        Historico.objects.create(
            conta=conta,
            operacao="Saque",
            valor=-valor,
            saldo=conta.saldo
        )
        return redirect('detalhes', conta_id=conta.id)  # Redireciona aos detalhes da conta

    return render(request, 'contas/sacar.html', {'conta': conta})

def transferir(request, conta_id):
    conta_origem = get_object_or_404(ContaCorrente, id=conta_id)

    if request.method == 'POST':
        numero_conta_destino = request.POST.get('conta_destino')  # Número da conta destino
        valor = Decimal(request.POST.get('valor', '0'))  # Converte para Decimal

        try:
            # Busca a conta pelo número
            conta_destino = ContaCorrente.objects.get(numero_conta=numero_conta_destino)
            conta_origem.realizar_operacao('Transferência Enviada', valor, conta_destino)
            return redirect('detalhes', conta_id=conta_id)
        except ContaCorrente.DoesNotExist:
            return render(request, 'contas/transferir.html', {
                'conta': conta_origem,
                'error': 'Conta de destino inválida!',
            })
        except ValidationError as e:
            return render(request, 'contas/transferir.html', {
                'conta': conta_origem,
                'error': str(e),
            })

    return render(request, 'contas/transferir.html', {'conta': conta_origem})

def historico(request, conta_id):
    # Obtém a conta pelo ID
    conta = get_object_or_404(ContaCorrente, id=conta_id)
    # Filtra os históricos relacionados à conta
    historico = Historico.objects.filter(conta=conta).order_by('-data')
    # Passa a conta para o template
    return render(request, 'contas/historico.html', {'historico': historico, 'conta': conta})

# View para exibir a lista de clientes
def lista_clientes(request):
    contas = ContaCorrente.objects.all()
    return render(request, 'contas/lista_clientes.html', {'contas': contas})