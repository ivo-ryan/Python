# arquivo = open('modulo_05/aula_03/receita.txt')
# arquivo2 = open('modulo_05/aula_03/receitas/fast_food.txt')
# print(arquivo.read())
# arquivo.close()
# print(arquivo2.read())
# arquivo2.close()

with open('modulo_05/aula_03/receita.txt') as arq:
    print(arq.read())

with open('modulo_05/aula_03/receitas/fast_food.txt', 'a') as arquivo :
    arquivo.write(', Nobara volta à vida e ajuda no fim da batalha!')
    