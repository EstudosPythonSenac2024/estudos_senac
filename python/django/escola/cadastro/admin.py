from django.contrib import admin
from .models import Aluno, Curso, Turma, Contato

# Permite adicionar cursos ao criar um aluno
class CursoInline(admin.TabularInline):
    model = Aluno.cursos.through  # Relacionamento ManyToMany
    extra = 1  # Mostra um campo extra para adicionar novos cursos

class AlunoAdmin(admin.ModelAdmin):
    inlines = [CursoInline]  # Adiciona cursos dentro do formulário de aluno
    list_display = ('nome',)  # Mostra o nome do aluno na lista

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Curso)  # Ainda permite criar cursos separadamente
admin.site.register(Turma)  # Ainda permite criar turmas separadamente

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_envio')  # Exibe esses campos na lista
    search_fields = ('nome', 'email')  # Permite buscar mensagens
    list_filter = ('data_envio',)  # Filtro por data

admin.site.register(Contato, ContatoAdmin)