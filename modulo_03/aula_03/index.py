lista = [1, 3, 4, 5, 7, 8, 9, 0, 2.5, 5.4, 52]

lista[2] = "horse"

print(lista)

lista[3:10] = ["Dog", "Fish", "Sneyk"]

print(lista)

print(len(lista))

animes = [{
    "nome" : "Jujutsu kaisen",
    "autor": "Gege"
}, {
    "nome" : "One Piece",
    "autor" : "Oda"
}, {
    "nome" : "Solo Leveling",
    "Autor" : "desconhecido"
}]


print(animes)

for x in animes:
    print(x)


animes.remove({"nome" : "Jujutsu kaisen","autor" : "Gege"})
print(animes)

del animes[0]

print(animes)

lista.clear()
print(lista)

lista = ["a", "b", "c"]
lista2 = lista.copy()

print(lista)
print(lista2)

lista2.append("D")

print(lista2)
print(lista)
