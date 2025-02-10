from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Cliente, RegistroEstacionamento
from .forms import ClienteForm, EstacionamentoForm
from datetime import datetime


def dashboard(request):
    total_vagas = 50
    vagas_ocupadas = RegistroEstacionamento.objects.filter(hora_saida__isnull=True).count()
    vagas_disponiveis = total_vagas - vagas_ocupadas

    # 🔥 Pega todos os clientes cadastrados
    clientes = Cliente.objects.all()  

    # 🔥 Pega todos os registros de estacionamento
    registros = RegistroEstacionamento.objects.all()

    return render(request, 'core/dashboard.html', {
        'clientes': clientes,  # Passando os clientes
        'registros': registros,  # Passando os registros de estacionamento
        'vagas_ocupadas': vagas_ocupadas,
        'vagas_disponiveis': vagas_disponiveis,
    })
def cadastrar_cliente(request):
    clientes = Cliente.objects.all()  # Obtém todos os clientes cadastrados

    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastrar_cliente')  # Redireciona para atualizar a lista de clientes
    else:
        form = ClienteForm()

    return render(request, 'core/cadastro.html', {'form': form, 'clientes': clientes})

def registrar_entrada(request):
    if request.method == "POST":
        form = EstacionamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EstacionamentoForm()
    return render(request, 'core/registro_entrada.html', {'form': form})

def registrar_saida(request, id):
    """Registra a saída do veículo e calcula o valor a pagar."""
    registro = get_object_or_404(RegistroEstacionamento, id=id)

    if request.method == "POST":
        hora_saida = datetime.strptime(request.POST.get("hora_saida"), "%H:%M").time()
        registro.registrar_saida(hora_saida)
        return redirect('dashboard')

    return render(request, 'core/registrar_saida.html', {'registro': registro})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # <- Redireciona para o dashboard após editar
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'core/editar_cliente.html', {'form': form, 'cliente': cliente})

def deletar_cliente(request, id):
    """Deleta um cliente do banco de dados."""
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('cadastrar_cliente') 