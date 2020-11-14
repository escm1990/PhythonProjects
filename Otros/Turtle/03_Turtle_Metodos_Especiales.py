import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto

t.speed(10) #valores del 1-10, siendo 1 el mas lento y 10 el mas rapido
t.circle(10)
t.circle(50)
t.dot(30) #punto o círculo relleno XD

t.hideturtle()
t.speed(10)
t.circle(40)

t.showturtle()
t.circle(100)

t.setx(100)
t.sety(-200)

turtle.done() # dejar fija y abierta el lienzo