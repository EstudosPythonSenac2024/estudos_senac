from django import forms
from .models import ContaCorrente

class ContaForm(forms.ModelForm):
    class Meta:
        model = ContaCorrente
        fields = ['agencia', 'numero_conta', 'titular', 'saldo', 'limite_negativo']