import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto
t.speed(10)

'''
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
'''

# Creacion de un cuadrado XD
'''
for i in range(4):
    t.forward(100) #avanza 100
    t.right(90) #gira a la derecha 90°
'''

'''
t.circle(100)
t.circle(90)
t.circle(80)
t.circle(70)
t.circle(60)
t.circle(50)
t.circle(40)
t.circle(30)
t.circle(20)
t.circle(10)
'''

resultado = input("¿Quieres imprimir una figura?")

if resultado == "si":
    i=0
    while i <= 100:
        t.circle(i)
        i += 10
else:
    print("OK")

turtle.done() # dejar fija y abierta el lienzo

