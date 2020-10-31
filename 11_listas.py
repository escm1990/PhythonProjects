#creacion de una lista
dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

dia = dias[0] #obtener el primer valor de la lista
print(dia)

dias2 = dias[-1] #imprime el último elemento de la lista (se recorre de -1 hacia atras)
print(dias2) 

sublista = dias[0:6] #el "hasta" (elemento indice 6) no es incluido
print(sublista)

sublista2 = dias[:7] # iniciando desde la posicion cero, si NO se coloca el "desde"
print(sublista2)

sublista3 = dias[4:] #barre desde el indice 4 hasta el ultimo elemento de la lista
print(sublista3)

sublista4 = dias[:] #barre toda la lista
print(sublista4)

saltoLista = dias[1:6:2] #imprime desde el indice 1 hasta el 6 con un salto de 2 en 2
print(saltoLista)

inversoLista = dias[::-1] #inverso de la lista
print(inversoLista)