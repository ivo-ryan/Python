# def olamundo():
#     print("olá mundo!")


# def executar():
#     olamundo()

# executar()


# def nome_x(nome):
#     return print(f"O nome é {nome}")



# nome_x("Residência")


# def imprimir_imovel( nome, quartos, vagas_garagem = None ):
#     print("Titulo: ", nome)
#     print("Numeros de quartos: " , quartos)
#     if vagas_garagem != None :
#         print("Vagas na garagem: ", vagas_garagem)



# imprimir_imovel("Casa de Luxo", 8, 3)

def imprimir_nomes(**nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']} ")
    if nomes['nome'] == "Hellen":
        print("Vai dizer quando o que você está guardando aí no peito hein? ")


imprimir_nomes(nome = "Hellen" , sobrenome = "Neres")

