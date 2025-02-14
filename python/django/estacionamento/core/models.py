from django.db import models
from datetime import datetime, timedelta

class Cliente(models.Model):
    TIPOS_CLIENTE = (
        ('mensalista', 'Mensalista'),
        ('avulso', 'Avulso'),
    )

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    ano = models.IntegerField(default=2024)
    cor = models.CharField(max_length=20)
    marca = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=TIPOS_CLIENTE, default='avulso')

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"



class RegistroEstacionamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modelo_carro = models.CharField(max_length=50)
    placa = models.CharField(max_length=10, unique=True)
    data_entrada = models.DateField(auto_now_add=True)
    hora_entrada = models.TimeField(auto_now_add=True)
    hora_saida = models.TimeField(null=True, blank=True)
    status_pagamento = models.CharField(
        max_length=10, choices=[('pago', 'Pago'), ('pendente', 'A pagar')], default='pendente'
    )
    valor_pago = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    def calcular_valor(self):
        """Calcula o valor a pagar baseado no tempo estacionado."""
        if self.hora_saida:
            entrada = datetime.combine(self.data_entrada, self.hora_entrada)
            saida = datetime.combine(self.data_entrada, self.hora_saida)
            tempo_total = (saida - entrada).total_seconds() / 3600  # Converte segundos para horas
            
            preco_por_hora = 10.00  # Defina o valor por hora (R$ 10,00)
            total = tempo_total * preco_por_hora

            return round(total, 2)  # Arredonda para duas casas decimais
        
        return 0  # Retorna 0 se o veículo ainda estiver no estacionamento

    def registrar_saida(self, hora_saida):
        """Define a hora de saída e calcula o valor a pagar."""
        self.hora_saida = hora_saida
        self.valor_pago = self.calcular_valor()
        self.status_pagamento = "pendente"
        self.save()

    def __str__(self):
        return f"{self.modelo_carro} - {self.placa}"
