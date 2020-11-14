import turtle
import random

# crear pantalla
s = turtle.Screen()
s.title("Turtle Race")
#s.bgcolor("gray")

 #crear objeto
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#modificando jugadores
jugador1.hideturtle()
jugador1.speed(10)
jugador1.shape("turtle")
jugador1.color("green","green") #color de la tinta, color de la figura
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

jugador2.hideturtle()
jugador2.speed(10)
jugador2.shape("turtle")
jugador2.color("blue","blue") #color de la tinta, color de la figura
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

# crear las metas de llegadas
jugador1.penup()
jugador1.goto(200,200) # punto de llegada
jugador1.pendown()
jugador1.circle(40)

jugador2.penup()
jugador2.goto(200,-200) # punto de llegada
jugador2.pendown()
jugador2.circle(40)

# colocando los jugadores en la posicion inicial
jugador1.penup()
jugador1.goto(-250,225)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

# creacion del dado
dado = [1,2,3,4,5,6]

# movilizando jugadores
for i in range(20): # consideración de turnos para llegar a la meta
    if(jugador1.pos() >= (200,200)):
        print("Jugador1 ha ganado")
        break
    elif(jugador2.pos() >= (200,-200)):
        print("Jugador2 ha ganado")
        break
    else:
        # turno del jugador1
        turno1 = input("JUGADOR1 - Presiona la tecla ENTER para avanzar.")
        turno1 = random.choice(dado)
        print("Tu numero es: ",turno1,"\nAvanzas: ",turno1*20)
        jugador1.pendown()
        jugador1.forward(turno1*20)
        # turno del jugador2
        turno2 = input("JUGADOR2 - Presiona la tecla ENTER para avanzar.")
        turno2 = random.choice(dado)
        print("Tu numero es: ",turno2,"\nAvanzas: ",turno2*20)
        jugador2.pendown()
        jugador2.forward(turno2*20)

turtle.done() # dejar fija y abierta el lienzo