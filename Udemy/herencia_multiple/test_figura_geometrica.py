from cuadrado import Cuadrado

cuadrado = Cuadrado(4,"Rojo")
print(cuadrado.area())
print(cuadrado.color)

#Method Resolution Order
print(Cuadrado.mro())