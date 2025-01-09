# Dicionário com produtos e preços
precos_produtos = {
    "celular": 1500,
    "notebook": 3000,
    "tablet": 1200,
    "mouse": 100,
    "monitor": 650,
    "caixa de som": 120,
    "teclado": 150,

}

while True:
    # Input do usuário para nome do produto
    produto = input("Digite o nome do produto para consulta (ou 'sair' para encerrar): ").strip().lower()

    # Encerrar o programa
    if produto == "sair":
        print("Consulta encerrada.")
        break

    # Verificar se o produto existe no dicionário
    if produto in precos_produtos:
        print(f"O produto '{produto.capitalize()}' custa R${precos_produtos[produto]:.2f}")
    else:
        print("Produto não encontrado, tente novamente.")