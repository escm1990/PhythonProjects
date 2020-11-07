#Escribir un programa que solicite al usuario un vocal en minuscula,
#y luego una letra en mayúsculas. El programa debe convertir la letra 
#en minúscula y la vocal en mayúscula, y al final, deben ser concatenadas ambas

minuscula = input("Ingrese una vocal en minuscula: ")
mayuscula = input("Ingrese una letra en mayuscula: ")

print("La letra minuscula es: {}, la letra mayuscula es: {} y la combinacion de ambas es {}".format(minuscula.upper(),
mayuscula.lower(),minuscula.upper()+mayuscula.lower()))

#Hacer un programa que pida al usuario su nombre, su edad y su sexo y los muestre de la siguiente forma:
#Te llamas: <nombre>
#Tu edad es: <edad>
#Eres: <sexo>

nombre= input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
sexo = input("Escribe tu sexo: ")

print("Te llamas: <{}>\nTu edad es: <{}>\nEres: <{}>\n".format(nombre,edad,sexo))
