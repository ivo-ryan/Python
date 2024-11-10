palpite = 0
numero = 9

while True:
    print("Qual eh o numero correto")
    palpite = int(input("Isira o seu palpite! "))
    if palpite == numero : 
        print("Parabens voce acertou!") 
        break
    else: print("Voce errou de novo tu é burro é!")
else:
    print("Erro na aplicacao")
    print(bool(palpite))



