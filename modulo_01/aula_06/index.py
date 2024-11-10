idade = input("Quantos anos você têm ? ")

if int(idade) < 16:
    print("Você é menor de idade ")
elif int(idade) > 18:
    print("Você é maior de idade!")
else:
    print("Você ainda não é maior de idade")


idade = input("Olá nadador quantos anos você têm ? ")

if int(idade) > 4 and int(idade) < 8:
    print("Infantil A")
elif int(idade) > 7 and int(idade) < 11:
    print("Infantil B")
elif int(idade) > 10 and int(idade) < 14:
    print("Juvenil A")
elif int(idade) > 13 and int(idade) < 18:
    print("Juvenil B")
else:
    print("Tu é um adulto toma vergonha , vai logo pra natação!")
