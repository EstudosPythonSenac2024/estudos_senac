numero_secreto = 5

tentativa = int(input("Adivinhe o número secreto: "))

if tentativa == numero_secreto:
    print("Booaaaaaa!!! Você acertou o número secreto!")
elif tentativa < numero_secreto:
    print(f"Errou!!!! O número é maior que {tentativa}.")
else:
    print(f"Errou! O número é menor que {tentativa}.")