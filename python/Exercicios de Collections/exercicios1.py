# Lista de produtos cadastrados
lista_produtos = []

while True:
    # Input do usuário para nome do produto
    produto = input("Digite o nome do produto (ou 'sair' para encerrar): ").strip().lower()

    # Encerrar o programa
    if produto == "sair":
        print("Cadastro encerrado.")
        break

    # Verificar se já existe
    if produto in lista_produtos:
        print("Produto já existente, tente novamente.")
    else:
        lista_produtos.append(produto)
        print(f"Produto '{produto.capitalize()}' cadastrado com sucesso!")
        print("Lista atual de produtos:", [p.capitalize() for p in lista_produtos])