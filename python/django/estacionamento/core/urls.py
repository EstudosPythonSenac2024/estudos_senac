from django.urls import path
from .views import (
    dashboard, cadastrar_cliente, editar_cliente, deletar_cliente,
    registrar_entrada, registrar_saida
)

urlpatterns = [
    # Dashboard principal
    path('', dashboard, name='dashboard'),

    # Rotas de Cadastro de Clientes
    path('cadastro/', cadastrar_cliente, name='cadastrar_cliente'),
    path('cadastro/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('cadastro/deletar/<int:id>/', deletar_cliente, name='deletar_cliente'),

    # Rotas de Registro de Estacionamento
    path('registro/', registrar_entrada, name='registro_entrada'),
    path('saida/<int:id>/', registrar_saida, name='registrar_saida'),
]

