from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_clientes, name='lista_clientes'),  # Página inicial (lista de clientes)
    path('<int:conta_id>/', views.detalhes, name='detalhes'),  # Detalhes de uma conta específica
    path('<int:conta_id>/historico/', views.historico, name='historico'),  # Histórico
    path('<int:conta_id>/sacar/', views.sacar, name='sacar'),  # Saque
    path('<int:conta_id>/depositar/', views.depositar, name='depositar'),  # Depósito
    path('<int:conta_id>/transferir/', views.transferir, name='transferir'),  # Transferência
]
