from django import forms
from .models import Cliente, RegistroEstacionamento

class ClienteForm(forms.ModelForm):
    ano = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Ex: 2025'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'modelo', 'placa', 'ano', 'cor', 'marca', 'tipo']

class EstacionamentoForm(forms.ModelForm):
    class Meta:
        model = RegistroEstacionamento
        fields = '__all__'
        exclude = ['valor_pago']


