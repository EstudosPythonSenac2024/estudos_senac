from django.contrib import admin
from .models import ContaCorrente, Historico

@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('titular', 'numero_conta', 'agencia', 'saldo')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('id', 'operacao', 'valor', 'data')  # Certifique-se de que os campos existem no modelo
    list_filter = ('operacao', 'data')  # Filtrar usando campos válidos do modelo