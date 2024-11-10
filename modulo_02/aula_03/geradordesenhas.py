

chave = input("Digite a base da sua senha: ")

senha = ""

for l in chave:
    if l in "Aa": senha = senha + "4"
    elif l in "Ee": senha = senha + "&"
    elif l in "Ii": senha = senha + "!"
    elif l in "Oo": senha = senha + "0"
    elif l in "Bb": senha = senha + "$"
    elif l in "Tt": senha = senha + "7"
    elif l in "Cc": senha = senha + "<"
    else : senha = senha + l

print(senha)