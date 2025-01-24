from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial com a lista de contas
    path('criar/', views.criar_conta, name='criar_conta'),
    path('<str:numero_conta>/', views.exibir_conta, name='exibir_conta'),
    path('<str:numero_conta>/depositar/', views.depositar, name='depositar'),
    path('<str:numero_conta>/sacar/', views.sacar, name='sacar'),
    path('<str:numero_conta>/transferir/', views.transferir, name='transferir'),
    path('<str:numero_conta>/historico/', views.historico, name='historico'),
]
