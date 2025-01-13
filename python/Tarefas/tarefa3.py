import random  # Importando o random para gerar números aleatórios

def escolher_dificuldade():
    while True: 
        print("Escolha o nível de dificuldade:")
        print("1. Fácil (30 tentativas, perde 10 pontos por erro)")
        print("2. Médio (15 tentativas, perde 20 pontos por erro)")
        print("3. Difícil (5 tentativas, perde 50 pontos por erro)")

        try:
            dificuldade = int(input("Escolha uma opção (1, 2 ou 3): "))
        except ValueError:
            print("Entrada inválida! Escolha um número entre 1 e 3.")
            continue
        
        if dificuldade == 1:
            return 30, 10  
        elif dificuldade == 2:
            return 15, 20  
        elif dificuldade == 3:
            return 5, 50
        else:
            print("Opção inválida! Escolha uma opção válida (1, 2 ou 3).")

def jogar():
    # Gerando o número secreto aleatoriamente entre 10 e 100
    numero_secreto = random.randint(10, 100)
    pontos = 100  

    tentativas, pontos_por_erro = escolher_dificuldade()

    print(f"\nVocê tem {tentativas} tentativas para adivinhar o número secreto!")
    print(f"Você começa com {pontos} pontos.")

    while tentativas > 0:
        tentativas -= 1

        while True:
            try:
                tentativa = int(input("\nTente adivinhar o número secreto (entre 10 e 100): "))
                if tentativa < 10 or tentativa > 100:
                    print("Por favor, insira um número entre 10 e 100.")
                else:
                    break
            except ValueError:
                print("Entrada inválida! Por favor, insira um número válido entre 10 e 100.")
        
        if tentativa == numero_secreto:
            print(f"Parabéns, você acertou o número secreto! Sua pontuação final é {pontos}.")
            break
        elif tentativa < numero_secreto:
            pontos -= pontos_por_erro
            print(f"Errou! O número secreto é maior que {tentativa}.")
        else:
            pontos -= pontos_por_erro
            print(f"Errou! O número secreto é menor que {tentativa}.")

        print(f"Você tem {tentativas} tentativas restantes e {pontos} pontos.")

    if tentativas == 0:
        print(f"\nVocê não conseguiu adivinhar o número secreto. Sua pontuação final é {pontos}.")

jogar()