from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:conta_id>/', views.detalhes, name='detalhes'),
    path('<int:conta_id>/depositar/', views.depositar, name='depositar'),
    path('<int:conta_id>/sacar/', views.sacar, name='sacar'),
    path('<int:conta_id>/transferir/', views.transferir, name='transferir'),
    path('<int:conta_id>/historico/', views.historico, name='historico'),
]
