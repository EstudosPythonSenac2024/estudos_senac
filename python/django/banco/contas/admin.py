from django.contrib import admin
from .models import ContaCorrente, Historico

@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_display = ('titular', 'numero_conta', 'agencia', 'saldo')

@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('conta', 'operacao', 'valor', 'data')
    list_filter = ('operacao', 'data')