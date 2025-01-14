class ContaCorrente:
    def __init__(self, agencia, numero_conta, titular, saldo_inicial=0):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    def consultar(self):
        print(f"Saldo atual da conta {self.numero_conta} - Agência: {self.agencia}, Titular: {self.titular}: R$ {self.saldo:.2f}")
        return self.saldo

    def sacar(self, valor):
        if valor <= 0:
            print("O valor do saque deve ser maior que zero.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para saque!")
        else:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            self.consultar()

    def depositar(self, valor):
        if valor < 0:
            print("O valor do depósito deve ser maior ou igual a zero.")
            return
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        self.consultar()

    def transferir(self, valor, conta_destino):
        if valor <= 0:
            print("O valor da transferência deve ser maior que zero.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para transferência!")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor
            print(f"Transferência de R$ {valor:.2f} concluída com sucesso para {conta_destino.titular}!")
            self.consultar()

# Exemplo de uso
def main():
    # Criação de contas
    conta1 = ContaCorrente("001", "12345-6", "João Silva", 1000)
    conta2 = ContaCorrente("002", "67890-1", "Maria Santos", 500)

    # Consulta inicial
    conta1.consultar()
    conta2.consultar()

    print("\n--- Operações Bancárias ---")

    # Saque
    conta1.sacar(200)

    # Depósito
    conta2.depositar(300)

    # Transferência
    conta1.transferir(300, conta2)

    # Consulta final
    conta1.consultar()
    conta2.consultar()

if __name__ == "__main__":
    main()