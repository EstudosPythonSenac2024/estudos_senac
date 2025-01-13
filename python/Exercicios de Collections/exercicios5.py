# Exercício 1
'''
Crie um sistema de consulta de preços
Seu sistema deve:
- Pedir para o usuário o nome de um produto
- Caso o produto exista na lista de produtos, o programa deve retornar o preço do produto como resposta
- Ex: O produto celular custa R$1500
- Caso o produto não exista na lista de produtos, o programa deve printar uma mensagem para o usuário tentar novamente
precos = {"celular": 1500, "camera": 1000, "fone de ouvido": 800, "monitor": 2000}
'''
precos = {"celular": 1500, 
          "camera": 1000, 
          "fone de ouvido": 800, 
          "monitor": 2000
          }

while True:
    # Input do usuário para nome do produto
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip().lower()
    print(f"DEBUG: Produto digitado: {produto}")
        # Encerrar o programa
    if produto == "sair":
        print("Consulta encerrada.")
        break

    if produto in precos:
        print(f'O {produto} custa R${precos[produto]}.')
    else: 
        print(f'O {produto} não existe, tente novamente.')