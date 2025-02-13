# Generated by Django 5.1.5 on 2025-01-30 00:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='curso',
        ),
        migrations.AddField(
            model_name='aluno',
            name='cursos',
            field=models.ManyToManyField(to='cadastro.curso'),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='turma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.turma'),
        ),
    ]
