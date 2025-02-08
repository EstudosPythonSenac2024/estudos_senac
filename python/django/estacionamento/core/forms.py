from django import forms
from .models import Cliente, RegistroEstacionamento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class EstacionamentoForm(forms.ModelForm):
    class Meta:
        model = RegistroEstacionamento
        fields = '__all__'
        exclude = ['valor_pago']
