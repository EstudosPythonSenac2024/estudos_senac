from django.urls import path
from . import views

urlpatterns = [
    path('<str:numero_conta>/depositar/', views.depositar, name='depositar'),
    path('<str:numero_conta>/sacar/', views.sacar, name='sacar'),
    path('<str:numero_conta>/transferir/', views.transferir, name='transferir'),
    path('criar_conta/', views.criar_conta, name='criar_conta'),
    path('<str:numero_conta>/historico/', views.historico, name='historico'),
]