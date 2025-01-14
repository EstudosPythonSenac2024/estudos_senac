import json
import os

class ContaCorrente:
    def __init__(self, agencia, numero_conta, titular, saldo_inicial=0, limite_negativo=-1000):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_negativo = limite_negativo
        self.historico = []  # Lista para guardar histórico de transações

    def salvar_historico(self):
        """Salva histórico no arquivo JSON"""
        data = {
            "agencia": self.agencia,
            "numero_conta": self.numero_conta,
            "titular": self.titular,
            "saldo": self.saldo,
            "limite_negativo": self.limite_negativo,
            "historico": self.historico,
        }
        with open(f"{self.numero_conta}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Histórico salvo em {self.numero_conta}.json\n")

    def carregar_historico(self):
        """Carrega histórico do arquivo JSON se existir"""
        if os.path.exists(f"{self.numero_conta}.json"):
            with open(f"{self.numero_conta}.json", "r") as file:
                data = json.load(file)
                self.saldo = data["saldo"]
                self.historico = data["historico"]
                print(f"Dados carregados para {self.numero_conta}\n")

    def adicionar_historico(self, operacao, valor):
        """Adiciona registro de operação no histórico"""
        self.historico.append({"operacao": operacao, "valor": valor, "saldo": self.saldo})

    def consultar(self):
        print(f"Saldo atual da conta {self.numero_conta} - Agência: {self.agencia}, Titular: {self.titular}: R$ {self.saldo:.2f}")
        return self.saldo

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        if self.saldo - valor < self.limite_negativo:
            print("Limite de saldo negativo atingido! Saque não permitido.")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            self.adicionar_historico("Saque", valor)
            self.consultar()
            self.salvar_historico()

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser maior que zero.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        self.adicionar_historico("Depósito", valor)
        self.consultar()
        self.salvar_historico()

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
            return
        if self.saldo - valor < self.limite_negativo:
            print("Limite de saldo negativo atingido! Transferência não permitida.")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R$ {valor:.2f} concluída com sucesso para {conta_destino.titular}!")
            self.adicionar_historico("Transferência Enviada", valor)
            conta_destino.adicionar_historico("Transferência Recebida", valor)
            self.consultar()
            self.salvar_historico()
            conta_destino.salvar_historico()

    def quitar_saldo_negativo(self):
        """Permite quitar o saldo negativo com 6% de taxa sobre o valor pago"""
        if self.saldo >= 0:
            print("Você não está com saldo negativo!")
            return

        print(f"Seu saldo negativo é de R$ {abs(self.saldo):.2f}")
        valor_pagamento = float(input("Digite o valor para quitar o saldo negativo: R$ "))

        if valor_pagamento <= 0:
            print("O valor de pagamento deve ser maior que zero.")
            return

        taxa = valor_pagamento * 0.06
        valor_com_taxa = valor_pagamento - taxa

        print(f"Valor da taxa (6%): R$ {taxa:.2f}")
        print(f"Valor final a ser aplicado após taxa: R$ {valor_com_taxa:.2f}")

        if abs(self.saldo) <= valor_com_taxa:
            self.saldo += valor_com_taxa
            print("Saldo negativo quitado com sucesso!")
        else:
            self.saldo += valor_com_taxa
            print(f"Saldo ainda negativo de R$ {abs(self.saldo):.2f}. Continue pagando para quitar totalmente.")

        self.adicionar_historico("Quitação de Saldo Negativo", valor_pagamento)
        self.consultar()
        self.salvar_historico()

def criar_conta():
    agencia = input("Digite a agência: ")
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    saldo_inicial = float(input("Digite o saldo inicial: R$ "))
    conta = ContaCorrente(agencia, numero_conta, titular, saldo_inicial)
    conta.carregar_historico()
    return conta

def menu():
    print("\n--- Menu de Operações ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Quitar saldo negativo")
    print("6. Sair")

def main():
    print("### Bem-vindo ao Sistema Bancário ###")
    conta1 = criar_conta()
    conta2 = criar_conta()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta1.consultar()
        elif opcao == "2":
            valor = float(input("Digite o valor para depósito: R$ "))
            conta1.depositar(valor)
        elif opcao == "3":
            valor = float(input("Digite o valor para saque: R$ "))
            conta1.sacar(valor)
        elif opcao == "4":
            valor = float(input("Digite o valor para transferência: R$ "))
            conta1.transferir(valor, conta2)
        elif opcao == "5":
            conta1.quitar_saldo_negativo()
        elif opcao == "6":
            print("Saindo... Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()