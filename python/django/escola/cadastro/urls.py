from django.urls import path
from .views import lista_alunos, contato

urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path('contato/', contato, name='contato'),
]