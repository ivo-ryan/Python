lista = ["One", "two", "TypeScript", 20 , False]

print(lista)
print(lista[-3])

animes = ["Jujutsu kaisen", "Solo Leveling", "Demon king Academy", "One Piece", "Classroom Of The Elite", "Nanatsu No Taizai", "Demon Slayer"]

print(animes[4:])
print(animes[0::4])
print(animes[:4])
print(animes[2:5])
print(animes[0:6:2])

lista += animes
print(lista)

print(len(lista))

lista2 = [21, 2, 3, 54, 6, 5, 87, 2.4]
lista3 = [0.9, 0.8, 2.9, 3.5, 5.6]

print(sum(lista2))
print(max(lista2))
print(min(lista3))

print(min(lista2))

nome = "Toji Fushiguro"
print(list(nome))