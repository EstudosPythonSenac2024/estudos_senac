from datetime import datetime

def calcular_idade(data_nascimento):    
    data_atual = datetime.now()
    dia, mes, ano = map(int, data_nascimento.split('/'))
    idade = data_atual.year - ano
    if (mes, dia > data_atual.month, data_atual.day):
        idade -= 1

    return idade

data_nascimento = input ("Entre o ano:")
idade = calcular_idade(data_nascimento)
print(f"Idade: {idade} anos")
