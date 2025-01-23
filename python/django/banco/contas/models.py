from django.db import models

class ContaCorrente(models.Model):
    agencia = models.CharField(max_length=10)
    numero_conta = models.CharField(max_length=20, unique=True)
    titular = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    limite_negativo = models.DecimalField(max_digits=10, decimal_places=2, default=-2000)

    def __str__(self):
        return f"{self.titular} - Conta: {self.numero_conta}"

class Historico(models.Model):
    conta = models.ForeignKey(ContaCorrente, on_delete=models.CASCADE, related_name='historico')
    operacao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.operacao} - R$ {self.valor:.2f} ({self.data.strftime('%d/%m/%Y %H:%M')})"
