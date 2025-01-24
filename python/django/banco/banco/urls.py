from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # Acesso ao Django Admin
    path('', include('contas.urls')),      # Rota principal redireciona para o app 'contas'
]