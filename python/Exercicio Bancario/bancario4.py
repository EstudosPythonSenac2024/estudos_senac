import json
import os

class ContaCorrente:
    def __init__(self, agencia, numero_conta, titular, saldo_inicial=0, limite_negativo=-1000):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial
        self.limite_negativo = limite_negativo
        self.historico = []

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
        with open(f"contas/{self.numero_conta}.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"Conta {self.numero_conta} salva com sucesso!\n")

    def carregar_historico(self):
        """Carrega histórico do arquivo JSON se existir"""
        if os.path.exists(f"contas/{self.numero_conta}.json"):
            with open(f"contas/{self.numero_conta}.json", "r") as file:
                data = json.load(file)
                self.saldo = data["saldo"]
                self.historico = data["historico"]
                print(f"Dados carregados para {self.numero_conta}\n")

    def adicionar_historico(self, operacao, valor):
        """Adiciona registro de operação no histórico"""
        self.historico.append({"operacao": operacao, "valor": valor, "saldo": self.saldo})

    def consultar(self):
        print(f"Saldo atual da conta {self.numero_conta} - Agência: {self.agencia}, Titular: {self.titular}: R$ {self.saldo:.2f}")

def carregar_contas_existentes():
    """Carrega todas as contas salvas em arquivos JSON na pasta 'contas'"""
    contas = []
    if not os.path.exists("contas"):
        os.makedirs("contas")

    for arquivo in os.listdir("contas"):
        if arquivo.endswith(".json"):
            with open(f"contas/{arquivo}", "r") as file:
                data = json.load(file)
                conta = ContaCorrente(
                    data["agencia"],
                    data["numero_conta"],
                    data["titular"],
                    data["saldo"],
                    data["limite_negativo"]
                )
                conta.historico = data["historico"]
                contas.append(conta)
    print(f"{len(contas)} contas carregadas com sucesso!")
    return contas

def criar_conta():
    """Cadastra uma nova conta e salva no JSON"""
    print("\n--- Cadastro de Nova Conta ---")
    agencia = input("Digite a agência: ")
    numero_conta = input("Digite o número da conta: ")
    titular = input("Digite o nome do titular: ")
    saldo_inicial = float(input("Digite o saldo inicial: R$ "))
    conta = ContaCorrente(agencia, numero_conta, titular, saldo_inicial)
    conta.salvar_historico()  # Salva imediatamente após cadastro
    print(f"Conta de {titular} cadastrada com sucesso!")
    return conta

def menu():
    print("\n--- Menu de Operações ---")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Quitar saldo negativo")
    print("6. Cadastrar nova conta")
    print("7. Listar contas cadastradas")
    print("8. Sair")

def escolher_conta(contas):
    """Permite escolher uma conta para realizar operações"""
    if len(contas) == 0:
        print("Não há contas cadastradas.")
        return None
    for i, conta in enumerate(contas):
        print(f"{i + 1}. {conta.titular} - Conta: {conta.numero_conta}")
    opcao = int(input("Escolha uma conta: ")) - 1
    if 0 <= opcao < len(contas):
        return contas[opcao]
    else:
        print("Opção inválida.")
        return None

def main():
    contas = carregar_contas_existentes()  # Carrega todas as contas na inicialização

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            conta = escolher_conta(contas)
            if conta:
                conta.consultar()
        elif opcao == "2":
            conta = escolher_conta(contas)
            if conta:
                valor = float(input("Digite o valor para depósito: R$ "))
                conta.depositar(valor)
        elif opcao == "3":
            conta = escolher_conta(contas)
            if conta:
                valor = float(input("Digite o valor para saque: R$ "))
                conta.sacar(valor)
        elif opcao == "4":
            print("Conta de origem:")
            conta_origem = escolher_conta(contas)
            print("Conta de destino:")
            conta_destino = escolher_conta(contas)
            if conta_origem and conta_destino:
                valor = float(input("Digite o valor para transferência: R$ "))
                conta_origem.transferir(valor, conta_destino)
        elif opcao == "5":
            conta = escolher_conta(contas)
            if conta:
                conta.quitar_saldo_negativo()
        elif opcao == "6":
            nova_conta = criar_conta()
            contas.append(nova_conta)  # Adiciona a conta à lista após cadastro
        elif opcao == "7":
            print("\n--- Contas Cadastradas ---")
            if contas:
                for conta in contas:
                    print(f"{conta.titular} - Conta: {conta.numero_conta} - Saldo: R$ {conta.saldo:.2f}")
            else:
                print("Não há contas cadastradas.")
        elif opcao == "8":
            print("Saindo... Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()