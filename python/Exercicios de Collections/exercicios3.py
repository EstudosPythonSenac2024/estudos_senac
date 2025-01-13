# Exercício 3
'''
Crie um sistema de consulta de bônus dos funcionários
Seu sistema deve:
- Pegar o valor de vendas do funcinoário por meio de um input
- Calcular o bônus do funcionário de acordo com a seguinte regra:
- Se o funcionário vendeu mais de 1000 unidades, ele ganha R$2 de bonus para cada unidade vendida
- Se o funcionário vendeu mais de 5000 unidades, ele ganha R$2 de bônus para cada unidade + um valor fixo de R$1000
- Se o funcionário vendeu menos de 1000 unidades, ele não ganha bônus 
- Printar no final o valor do bônus do funcionário
'''

while True:
    # Entrada do nome do funcionário
    funcionario = input("Digite o nome do funcionário (ou 'sair' para encerrar): ").strip().capitalize()

    # Encerrar o programa
    if funcionario.lower() == "sair":
        print("Consulta encerrada.")
        break

    # Entrada da quantidade de vendas
    try:
        vendas = int(input(f"Digite a quantidade de vendas de {funcionario}: "))
    except ValueError:
        print("Por favor, insira um número válido para as vendas.")
        continue

    # Cálculo do bônus
    if vendas > 1000:
        bonus = vendas * 2
        if vendas > 5000:
            bonus += 1000  # Bônus extra de R$ 1000 para mais de 5000 unidades
        print(f"{funcionario} vendeu {vendas} unidades e recebeu um bônus de R${bonus:.2f}")
    else:
        print(f"{funcionario} vendeu apenas {vendas} unidades e não tem direito a bônus.")

    print("-" * 40)  # Linha de separação para organização