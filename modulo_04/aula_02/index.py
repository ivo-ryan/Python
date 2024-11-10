animes = {"anime1" : "Jujutsu Kaisen", "anime2" : "Nanatsu No Taizai" }

print(animes["anime2"])

print(animes.keys())
print(animes.values())
print(animes.items())


if "anime1" in animes:
    print(f"O anime {animes['anime1']} existe")
else: print("O anime ainda nao foi adicionado")

tupla = ("item1", "item2", "item3")

dicio = dict.fromkeys(tupla)

print(dicio)

