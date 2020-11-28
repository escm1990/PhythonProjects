'''escriba un script que solicite ingresar al usuario una cantidad de dinero a invertir, el interés anual que el
banca pagará y el número de años. El script deberá calcular e imprimir el capital total obtenido por la inversión de la
persona.'''

import math

dineroInvertir = float(input("Ingrese la cantidad de dinero a invertir: "))
interesAnual = float(input("Ingrese el interés anual: "))
anios = int(input("Ingrese la cantidad de años a calcular: "))

S = round(dineroInvertir*math.pow((1+interesAnual/100),anios),2)

print("El capital a obtener será de: "+str(S))