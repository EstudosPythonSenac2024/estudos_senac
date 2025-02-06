from django.urls import path
from .views import lista_alunos, contato  # 🔹 Remova "views"

urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path('contato/', contato, name='contato'),  # 🔹 Agora chamamos "contato" diretamente
]
