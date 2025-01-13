def escolher_dificuldade():
    while True: 
        #Escolha de dificuldade do jogador com o input abaixo#
        print("Escolha o nível de dificuldade:")
        print("1. Fácil (30 tentativas, perde 10 pontos por erro)")
        print("2. Médio (15 tentativas, perde 20 pontos por erro)")
        print("3. Difícil (5 tentativas, perde 50 pontos por erro)")


        try:
            dificuldade = int(input("Escolha uma opção (1, 2 ou 3): "))
        except ValueError:
            print("Entrada inválida! Por favor, escolha um número entre 1 e 3.")
            continue
        
        if dificuldade == 1:
            return 30, 10  
            
        elif dificuldade == 2:
            return 15, 20  
        elif dificuldade == 3:
            return 5, 50
        else:
            print("Opção inválida! Por favor, escolha uma opção válida (1, 2 ou 3).")
def jogar():
    numero_secreto = 5
    pontos = 100  

   
    tentativas, pontos_por_erro = escolher_dificuldade()


    print(f"\nVocê tem {tentativas} tentativas para adivinhar o número secreto!")
    print(f"Você começa com {pontos} pontos.")

    while tentativas > 0:
        tentativas -= 1

       
        try:
            tentativa = int(input("\nTente adivinhar o número secreto: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")
            continue
        if tentativa == numero_secreto:
            print(f"BOAAAAAAA!!! Acertou o número secreto! Sua pontuação final é {pontos}.")
            break
        elif tentativa < numero_secreto:
            tentativas -= 1
            pontos -= pontos_por_erro
            print(f"Errou! O número secreto é maior que {tentativa}.")
        else:
            tentativas -= 1
            pontos -= pontos_por_erro
            print(f"Errou! O número secreto é menor que {tentativa}.")

       
        print(f"Você tem {tentativas} tentativas restantes e {pontos} pontos.")

    if tentativas == 0:
        print(f"\nVocê não conseguiu adivinhar o número secreto. Sua pontuação final é {pontos}.")

jogar()