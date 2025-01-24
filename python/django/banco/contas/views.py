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



def exibir_conta(request, numero_conta):
    """Exibe os detalhes de uma conta específica."""
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    return render(request, 'contas/exibir_conta.html', {'conta': conta})


def depositar(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    if request.method == 'POST':
        valor = float(request.POST['valor'])
        if valor > 0:
            conta.realizar_operacao("Depósito", valor)
            messages.success(request, f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            messages.error(request, "O valor do depósito deve ser maior que zero.")
        return redirect('exibir_conta', numero_conta=numero_conta)
    return render(request, 'contas/depositar.html', {'conta': conta})



def sacar(request, numero_conta):
    """View para realizar saques de uma conta."""
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)

    if request.method == 'POST':
        valor = float(request.POST['valor'])
        try:
            conta.realizar_operacao("Saque", valor)
            messages.success(request, f"Saque de R$ {valor:.2f} realizado com sucesso!")
        except Exception as e:
            messages.error(request, str(e))
        return redirect('exibir_conta', numero_conta=numero_conta)

    return render(request, 'contas/sacar.html', {'conta': conta})


def transferir(request, numero_conta):
    """View para realizar transferências entre contas."""
    conta_origem = get_object_or_404(ContaCorrente, numero_conta=numero_conta)

    if request.method == 'POST':
        numero_destino = request.POST['numero_destino']
        valor = float(request.POST['valor'])

        try:
            conta_destino = ContaCorrente.objects.get(numero_conta=numero_destino)
            conta_origem.realizar_operacao("Transferência Enviada", valor, conta_destino=conta_destino)
            messages.success(request, f"Transferência de R$ {valor:.2f} realizada com sucesso!")
        except ContaCorrente.DoesNotExist:
            messages.error(request, "Conta de destino não encontrada.")
        except Exception as e:
            messages.error(request, str(e))
        return redirect('exibir_conta', numero_conta=numero_conta)

    return render(request, 'contas/transferir.html', {'conta_origem': conta_origem})


def historico(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    historico = conta.historico.all().order_by('-data')
    
    # Paginação
    paginator = Paginator(historico, 10)  # Mostra 10 operações por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'contas/historico.html', {
        'conta': conta,
        'page_obj': page_obj
    })
