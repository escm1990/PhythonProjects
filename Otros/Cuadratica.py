#3x^2-5x+2=0    x=1     x=2/3

import math

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

raiz = math.pow(b,2)-(4*a*c)

if raiz<0:
    print("No es posible calcular raíces negativas")
else:
    x1 = (-b-math.sqrt(raiz))/(2*a)
    x2 = (-b+math.sqrt(raiz))/(2*a)
    print("x1 = {}".format(x1))
    print("x2 = {}".format(x2))
