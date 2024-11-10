usuario = input("Digite um nome: ")


def minha_funcao(nome):
    if nome == "Ryan": print("O nome esta correto")
    elif nome == "Hellen" :
        print("Será que ela é a escolhida?")
        input("Responda o que você acha: ")
        print("Então oque você acha de esperar até se reencontrarem novamente ?")
        input("Responda: ")
        print("Deus nos mostrará se ela for a escolhida!")
    else: print("O nome esta errado")

minha_funcao(usuario)

# numero = int(input("Digite um numero: "))

# def par_impar(num):
#     if (num % 2) == 0 :
#         return print("É um número par!")
#     else : return print("É um número impar!")


# par_impar(numero)