'''Escriba un script que muestre al usuario las siguientes opciones en un menú: convertir libras a kilos,
convertir kilos a libras, convertir euros a dólares y convertir dólares a euros. En base a la selección del usuario el script
deberá solicitar al usuario la información necesaria para realizar la conversión que haya seleccionado. Finalmente debe
mostrar en pantalla el resultado de la conversión.'''

print("*******CONVERTIDOR DE UNIDADES*********")
print("1 - Libras a Kilos\n2 - Kilos a Libras\n3 - Euros a Dolares\n4 - Dolares a Euros")
opcion = int(input("Ingrese la opción de conversión que desea utilizar: "))
resultado = 0

if opcion == 1:
    print("Libras a Kilos")
    entrada = float(input("Ingresa la cantidad en Libras: "))
    resultado = round(entrada*0.453592,2)
elif opcion == 2:
    print("Kilos a Libras")
    entrada = float(input("Ingresa la cantidad en Kilogramos: "))
    resultado = round(entrada*2.20462,2)
elif opcion == 3:
    print("Euros a Dolares")
    entrada = float(input("Ingresa la cantidad en Euros: "))
    resultado = round(entrada*1.19,2)
elif opcion == 4:
    print("Dolares a Euros")
    entrada = float(input("Ingresa la cantidad en Dolares: "))
    resultado = round(entrada*0.84,2)

print("El resultado de la conversión es: {} ".format(resultado))