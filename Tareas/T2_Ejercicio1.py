#Calcular el área de un triángulo

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = round((base*altura)/2,2)

print("El area del triángulo es: {}".format(area))