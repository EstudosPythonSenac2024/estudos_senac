# Criar a view para listar alunos em cadastro/views.py

from django.shortcuts import render
from .models import Aluno,Curso, Turma
from collections import Counter
import json

#def lista_alunos(request):
#    alunos = Aluno.objects.all()
#    return render(request, 'cadastro/lista_alunos.html', {'alunos': alunos})

def contato(request):
    return render(request, 'cadastro/contato.html')

def lista_alunos(request):
    alunos = Aluno.objects.all()

    # Contar a quantidade de alunos em cada curso
    cursos_count = Counter()
    turmas_count = Counter()

    for aluno in alunos:
        for curso in aluno.cursos.all():  # Agora considerando múltiplos cursos
            cursos_count[curso.nome] += 1
        turmas_count[aluno.turma.nome] += 1  # Contagem de turmas

    # Criar listas para os gráficos de pizza
    cursos_labels = list(cursos_count.keys())
    cursos_values = list(cursos_count.values())

    turmas_labels = list(turmas_count.keys())
    turmas_values = list(turmas_count.values())

    # Criar estrutura de dados para os gráficos Sankey
    sankey_curso_turma = []
    for aluno in alunos:
        for curso in aluno.cursos.all():
            sankey_curso_turma.append([curso.nome, aluno.turma.nome, 1])

    sankey_aluno_curso_turma = []
    for aluno in alunos:
        for curso in aluno.cursos.all():
            sankey_aluno_curso_turma.append([aluno.nome, curso.nome, 1])  # Aluno → Curso
            sankey_aluno_curso_turma.append([curso.nome, aluno.turma.nome, 1])  # Curso → Turma

    context = {
        'alunos': alunos,
        'cursos_labels': json.dumps(cursos_labels),
        'cursos_values': json.dumps(cursos_values),
        'turmas_labels': json.dumps(turmas_labels),
        'turmas_values': json.dumps(turmas_values),
        'sankey_data_curso_turma': json.dumps(sankey_curso_turma),
        'sankey_data_aluno_curso_turma': json.dumps(sankey_aluno_curso_turma),
    }

    return render(request, 'cadastro/lista_alunos.html', context)




