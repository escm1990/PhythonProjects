import turtle

# crear pantalla
s = turtle.Screen()
t = turtle.Turtle() #crear objeto
'''
t.backward(100) # moverse hacia atras una cantidad de pixeles
t.right(90) # definir direccion a la derecha, se le pasan grados como parametro
t.forward(90) # moverse hacia la direccion 
t.left(90) # moverse a la izquierda
t.forward(100) # avanzar 100
'''

# lo mismo que el bloque anterior, solo que abreviado
t.bk(100)
t.rt(90)
t.fd(90)
t.lt(90)
t.fd(100)

turtle.done() # dejar fija y abierta el lienzo

