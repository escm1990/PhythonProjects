eltexto = "Python es una gran onda"
print(len(eltexto))

##################################

def calcula_longitud(lalongitud):
    contador = 0
    for caracter in lalongitud:
        contador += 1
    return contador

eltexto = "Python es una gran onda"
print(calcula_longitud(eltexto))
