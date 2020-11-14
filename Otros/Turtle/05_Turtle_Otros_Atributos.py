import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto

'''
t.begin_fill() # iniciar relleno
t.circle(100)
t.end_fill() # terminar relleno

t.begin_fill() # iniciar relleno
t.color("white","white")
t.circle(50)
t.end_fill() # terminar relleno
'''
t.shape("turtle")

t.forward(100)
t.penup() # levantar lapiz
t.forward(50)
t.pendown() # bajar lapiz
t.forward(100)

t.undo() # deshacer la ultima accion de la tortuga
t.clear() #limpiar toda la pantalla, pero la tortuga queda en el mismo lugar
t.reset() #el programa se reinicia por completo

t.forward(100)
t.stamp() # sello
t.forward(100)

turtle.done() # dejar fija y abierta el lienzo

