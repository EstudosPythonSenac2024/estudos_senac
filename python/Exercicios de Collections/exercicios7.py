precos = {
    "celular": 1500,
    "camera": 1000,
    "fone de ouvido": 800,
    "monitor": 3000
}

# Função para calcular o novo preço com base no reajuste
def aplicar_reajuste(preco):
    if preco <= 1000:
        return preco * 1.10  # Reajuste de 10%
    elif preco <= 2000:
        return preco * 1.15  # Reajuste de 15%
    else:
        return preco * 1.20  # Reajuste de 20%

# Calculando o novo preço para cada produto
novos_precos = {produto: aplicar_reajuste(preco) for produto, preco in precos.items()}

# Exibindo os novos preços
for produto, novo_preco in novos_precos.items():
    print(f"{produto}: R${novo_preco:.2f}")