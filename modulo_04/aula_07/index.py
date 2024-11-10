# def reduzir_numero(numero_int):
#     if numero_int > 0 :
#         print(numero_int)
#         reduzir_numero(numero_int -1 )


# reduzir_numero(10)


def fatorial_s(numero):
    fatorial = 1
    if numero == 0 :
        return 1
    else : 
        for x in range(1, numero + 1 ):
            fatorial *= x
        return fatorial
    

#print(fatorial_s(5))

def fatorial_r(numero_int):
    if numero_int == 0: return 1
    else : return numero_int * fatorial_r( numero_int - 1 )



print(fatorial_r(0))