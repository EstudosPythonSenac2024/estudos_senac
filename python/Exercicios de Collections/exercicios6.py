# Exercício 2
'''
Agora edite o programa anterior para fazer com que, caso não exista o produto, o programa pergunte se o usuário quer cadastrar o produto
Se ele responder sim, o programa deve pedir o nome do produto e o preco do produto e cadastrar no dicionário de preços
Em seguida do cadastro bem sucedido, o programa deve printar o dicionário de precos atualizado
'''
import json # Biblioteca para manipular JSON

# Nome do arquivo JSON onde os dados serão salvos
arquivo_json = "precos.json"

# Função para carregar os preços do arquivo JSON
def carregar_precos():
    try:
        with open(arquivo_json, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Se o arquivo não existir, cria um dicionário vazio
        return {}

# Função para salvar os preços no arquivo JSON
def salvar_precos(precos):
    with open(arquivo_json, "w") as f:
        json.dump(precos, f, indent=4)
    print("Dados salvos com sucesso!")

# Carrega os preços ao iniciar o programa
precos = carregar_precos()

while True:
    # Exibe os produtos atuais
    print("\nProdutos disponíveis:", precos)

    produto = input("\nDigite o nome do produto (ou 'sair' para encerrar): ").strip().lower()

    if produto == "sair":
        print("Programa encerrado.")
        break

    if produto in precos:
        print(f"O {produto} custa R${precos[produto]}.")
        # Opção de deletar o produto
        deletar = input("Deseja deletar este produto? (sim/não): ").strip().lower()
        if deletar == "sim":
            del precos[produto]
            print(f"Produto '{produto}' deletado com sucesso!")
            salvar_precos(precos) # Atualiza o arquivo
        else:
            print("Produto não deletado.")
    else:
        print(f"O {produto} não existe.")
        cadastrar = input("Deseja cadastrar este produto? (sim/não): ").strip().lower()
        
        if cadastrar == "sim":
            nome_produto = input("Digite o nome do novo produto: ").strip().lower()
            preco_produto = input("Digite o preço do novo produto: ").strip()

            if preco_produto.isdigit():
                precos[nome_produto] = int(preco_produto)
                print(f"Produto '{nome_produto}' cadastrado com sucesso!")
                salvar_precos(precos) # Atualiza o arquivo com o novo produto
            else:
                print("Preço inválido! O produto não foi cadastrado.")