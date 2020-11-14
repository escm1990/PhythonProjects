import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto

s.bgcolor("red") #BACKGROUnD del screen
s.title("Proyecto1") #modificar titulo

t.shapesize(3,3,3) #ancho, largo, borde
t.fillcolor("orange") # color de la tortura (relleno)
t.pencolor("white") # color de la linea y del borde
t.forward(100)

#otra forma de cambiar los atributos visuales de la tortuga
t.color("green","blue")
t.right(90)
t.forward(100)

t.pensize(5) #grosor de la línea
t.forward(100)

turtle.done() # dejar fija y abierta el lienzo

