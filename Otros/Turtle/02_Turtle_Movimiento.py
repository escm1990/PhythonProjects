import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto

t.goto(100,100) # colocar la coordenada a donde querramos que vaya
t.goto(-100,100)
t.home() # volver al punto 0,0

t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°
t.forward(100) #avanza 100
t.right(90) #gira a la derecha 90°

turtle.done() # dejar fija y abierta el lienzo