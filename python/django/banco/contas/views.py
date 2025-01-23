from django.shortcuts import render, get_object_or_404
from .models import ContaCorrente,Historico

def criar_conta(request):
    if request.method == 'POST':
        agencia = request.POST['agencia']
        numero_conta = request.POST['numero_conta']
        titular = request.POST['titular']
        saldo = float(request.POST.get('saldo', 0))
        limite_negativo = float(request.POST.get('limite_negativo', -2000))

        conta = ContaCorrente.objects.create(
            agencia=agencia,
            numero_conta=numero_conta,
            titular=titular,
            saldo=saldo,
            limite_negativo=limite_negativo
        )
        return render(request, 'conta_criada.html', {'conta': conta})

    return render(request, 'criar_conta.html')

def depositar(request, numero_conta):
    # Busca a conta pelo número
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)

    if request.method == 'POST':
        # Recebe o valor do depósito do formulário
        valor = float(request.POST['valor'])

        if valor > 0:
            # Atualiza o saldo da conta
            conta.saldo += valor
            conta.save()

            # Salva no histórico
            Historico.objects.create(
                conta=conta,
                operacao='Depósito',
                valor=valor
            )

            return render(request, 'contas/sucesso.html', {
                'mensagem': f"Depósito de R$ {valor:.2f} realizado com sucesso!"
            })
        else:
            return render(request, 'contas/erro.html', {
                'mensagem': "O valor do depósito deve ser maior que zero."
            })

    # Renderiza a página de depósito
    return render(request, 'contas/depositar.html', {'conta': conta})

def historico(request, numero_conta):
    # Busca a conta pelo número
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    # Recupera o histórico ordenado pela data mais recente
    historico = conta.historico.all().order_by('-data')

    return render(request, 'contas/historico.html', {
        'conta': conta,
        'historico': historico
    })

def sacar(request, numero_conta):
    # Busca a conta pelo número
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)

    if request.method == 'POST':
        valor = float(request.POST['valor'])

        if valor > 0:
            if conta.saldo - valor >= conta.limite_negativo:
                # Atualiza o saldo e salva
                conta.saldo -= valor
                conta.save()

                # Registra no histórico
                Historico.objects.create(
                    conta=conta,
                    operacao='Saque',
                    valor=-valor
                )

                return render(request, 'contas/sucesso.html', {
                    'mensagem': f"Saque de R$ {valor:.2f} realizado com sucesso!"
                })
            else:
                return render(request, 'contas/erro.html', {
                    'mensagem': "Saldo insuficiente para realizar o saque."
                })
        else:
            return render(request, 'contas/erro.html', {
                'mensagem': "O valor do saque deve ser maior que zero."
            })

    return render(request, 'contas/sacar.html', {'conta': conta})

def transferir(request, numero_conta):
    # Conta de origem
    conta_origem = get_object_or_404(ContaCorrente, numero_conta=numero_conta)

    if request.method == 'POST':
        numero_destino = request.POST['numero_destino']
        valor = float(request.POST['valor'])

        if valor > 0:
            # Busca a conta de destino
            try:
                conta_destino = ContaCorrente.objects.get(numero_conta=numero_destino)
            except ContaCorrente.DoesNotExist:
                return render(request, 'contas/erro.html', {
                    'mensagem': "Conta de destino não encontrada."
                })

            if conta_origem.saldo - valor >= conta_origem.limite_negativo:
                # Realiza a transferência
                conta_origem.saldo -= valor
                conta_destino.saldo += valor

                conta_origem.save()
                conta_destino.save()

                # Registra no histórico
                Historico.objects.create(
                    conta=conta_origem,
                    operacao='Transferência Enviada',
                    valor=-valor
                )
                Historico.objects.create(
                    conta=conta_destino,
                    operacao='Transferência Recebida',
                    valor=valor
                )

                return render(request, 'contas/sucesso.html', {
                    'mensagem': f"Transferência de R$ {valor:.2f} realizada com sucesso!"
                })
            else:
                return render(request, 'contas/erro.html', {
                    'mensagem': "Saldo insuficiente para realizar a transferência."
                })
        else:
            return render(request, 'contas/erro.html', {
                'mensagem': "O valor da transferência deve ser maior que zero."
            })

    return render(request, 'contas/transferir.html', {'conta_origem': conta_origem})

def criar_conta(request):
    if request.method == 'POST':
        agencia = request.POST['agencia']
        numero_conta = request.POST['numero_conta']
        titular = request.POST['titular']
        saldo_inicial = float(request.POST['saldo_inicial'])

        conta = ContaCorrente.objects.create(
            agencia=agencia,
            numero_conta=numero_conta,
            titular=titular,
            saldo=saldo_inicial
        )

        return render(request, 'contas/sucesso.html', {
            'mensagem': f"Conta de {titular} criada com sucesso!"
        })

    return render(request, 'contas/criar_conta.html')

def index(request):
    contas = ContaCorrente.objects.all()  # Recupera todas as contas
    return render(request, 'contas/index.html', {'contas': contas})

def exibir_conta(request, numero_conta):
    conta = get_object_or_404(ContaCorrente, numero_conta=numero_conta)
    return render(request, 'contas/exibir_conta.html', {'conta': conta})