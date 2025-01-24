from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now


class ContaCorrente(models.Model):
    agencia = models.CharField(max_length=10)
    numero_conta = models.CharField(max_length=20, unique=True)
    titular = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    limite_negativo = models.DecimalField(max_digits=10, decimal_places=2, default=-2000)

    def __str__(self):
        return f"{self.titular} - Conta: {self.numero_conta}"

    def realizar_operacao(self, tipo, valor, conta_destino=None):
        """
        Realiza operações como saque, depósito ou transferência.
        """
        if valor <= 0:
            raise ValidationError(f"O valor da operação '{tipo}' deve ser maior que zero.")

        if tipo == "Saque":
            if self.saldo - valor < self.limite_negativo:
                raise ValidationError("Saldo insuficiente para realizar o saque.")
            self.saldo -= valor

        elif tipo == "Depósito":
            self.saldo += valor

        elif tipo == "Transferência Enviada":
            if not conta_destino:
                raise ValidationError("Conta de destino não especificada para transferência.")
            if self.saldo - valor < self.limite_negativo:
                raise ValidationError("Saldo insuficiente para realizar a transferência.")
            self.saldo -= valor
            conta_destino.saldo += valor
            conta_destino.save()
            Historico.objects.create(
                conta=conta_destino,
                operacao="Transferência Recebida",
                valor=valor,
                saldo=conta_destino.saldo
            )

        # Salva as alterações e cria o histórico da operação
        self.save()
        Historico.objects.create(
            conta=self,
            operacao=tipo,
            valor=-valor if tipo == "Saque" or tipo == "Transferência Enviada" else valor,
            saldo=self.saldo
        )


class Historico(models.Model):
    conta = models.ForeignKey(ContaCorrente, on_delete=models.CASCADE, related_name='historico')
    operacao = models.CharField(max_length=50)  # Ex.: "Depósito", "Saque", "Transferência"
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.operacao} - R$ {self.valor:.2f} ({self.data.strftime('%d/%m/%Y %H:%M')})"
