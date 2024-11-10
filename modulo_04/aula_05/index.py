from random import choice

jogador_vitorias = 0
maq_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra , Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra" :
        return esc_jogador
    elif esc_jogador == "papel" :
        return esc_jogador
    elif esc_jogador == "tesoura" :
        return esc_jogador
    else : 
        print("Opção inválida! Tente novamente")
        Opcao_Jogador()

def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True :

    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
        or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        print(f"O Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina} "
              "Player Wins!!!!!")
        jogador_vitorias += 1

    elif esc_jogador == esc_maquina:
        print(f"O Jogador escolheu {esc_jogador} e a Máquina escolheu {esc_maquina} "
              "Empate!!!!!")
    else:
        print(f"A Máquina escolheu {esc_maquina} e o Jogador escolheu {esc_jogador }"
              " You Lose!!!")
        maq_vitorias += 1


    print("-"*30)
    print(f"Vitorias do jogador: {jogador_vitorias} ")
    print(f"Vitorias da maquina: {maq_vitorias} ")
    print("-"*30)

    esc_jogador = input("Você quer jogar novamente? ")
    if esc_jogador in ["SIM", "Sim", "sim", "S", "s"]:
        pass
    elif esc_jogador in ["NAO", "Nao", "nao", "N", "n"]:
        break
    else : break