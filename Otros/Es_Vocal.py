#Crear un programa que pida al usuario una letra, 
# y si es vocal, muestre el mensaje "Es vocal". 
# Sino, decirle al usuario que no es vocal

letra = input("Escribe una letra: ")

if letra.lower()=="a" or letra.lower()=="e" or letra.lower()=="i" or letra.lower()=="o" or letra.lower()=="u":
    print("Es vocal")
else:
    print("No es vocal")