from django.urls import path
from .views import dashboard, cadastrar_cliente, registrar_entrada, registrar_saida

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('cadastro/', cadastrar_cliente, name='cadastro_cliente'),
    path('registro/', registrar_entrada, name='registro_entrada'),
    path('saida/<int:id>/', registrar_saida, name='registrar_saida'),
]