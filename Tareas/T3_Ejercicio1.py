"""
En la siguiente lista, debes hacer un programa que muestre los valores de la misma al usuario,
a su vez, debe pedir dos datos y estos deben sustituir al primer y tercer elemento de la misma.
El primer valor solicitado debe ser una cadena de texto y el segundo un entero. Asimismo, crear 
una sublista que contenga los elementos desde el septimo al último elemento de la lista principal.
"""

lista =[20,50,"Curso","Python",3.14,40,"Futbol","X",8.75,10,"Programacion"] 

print("Lista principal: ",lista)

valor1= input("Ingrese el primer valor a sustituir (texto): ")
valor2 = int(input("Ingrese el segundo valor a sustituir (entero): "))

lista[0] = valor1
lista[2] = valor2

print("Lista con valores sustituidos: ",lista)

sublista = lista[6:]

print("La sublista requerida es: ",sublista)