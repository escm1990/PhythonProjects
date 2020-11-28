variable_uno = 5
variable_dos = 20

mayor = variable_uno > variable_dos

variable1 = [5,9,1,58,4,2.65,10.8]
variable2 = variable1.index(4)
print(variable2)

#cadena = "Bienvenidos al curso de Python"
#cambio = "b" + cadena[1:] + 3 +" "+"nivel básico."
#print(cambio)

cadena2 = "Bienvenidos al curso de Python nivel básico"
busqueda = cadena2.startswith("Bienvenidos")
print(busqueda)

print("---------------------------------------------")

a=7
b=10

if a>b:
    print('10 es mayor que 7')
elif a<b:
    print('7 es menor que 10')
elif a==b:
    print('Son iguales')

print("---------------------------------------------")


i = 0
while i <= 3:
    print(i)
    i+=1

print("---------------------------------------------")

lista = [1,2,3,4,5,6,7,8]
for valor in range(len(lista)):
    print(valor)