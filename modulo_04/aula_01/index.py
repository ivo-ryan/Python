tupla = ("item1", "item2", "item3", "item1", "item1")

print(tupla.count("item1"))

lista = list(tupla)
lista.append("item5")
print(lista)

tupla = tuple(lista)

print(tupla)


tupla = "item1", "item2"
tupla2 = "a", "b"

tupla3 = tupla + tupla2

print(tupla3)