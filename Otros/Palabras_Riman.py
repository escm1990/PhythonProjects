#Escribe un programa que pida dos palabras y diga si riman o no. 
#Si coinciden las tres últimas letras tiene que decir que riman. 
#Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input("Escriba la primer palabra: ")
palabra2 = input("Escriba la segunda palabra: ")

ult_tres_p1 = palabra1[-3:] 
ult_tres_p2 = palabra2[-3:]
ult_dos_p1 = palabra1[-2:]
ult_dos_p2 = palabra2[-2:]

if ult_tres_p1 == ult_tres_p2:
    print("Las palabras riman")
elif ult_dos_p1 == ult_dos_p2:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")
