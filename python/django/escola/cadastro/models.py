#from django.db import models

#class Aluno(models.Model):
#    nome = models.CharField(max_length=100)
#    curso = models.CharField(max_length=100)
#    turma = models.CharField(max_length=50)
#
#    def __str__(self):
#        return self.nome
    
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, blank=True)  # 🔹 Agora pode ter vários cursos
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
