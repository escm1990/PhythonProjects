tupla_uno = (5,10,15,30,50,100,110,200)
item = tupla_uno[3]
print(item)

item2 = tupla_uno[-3]
print(item2)

subtupla = tupla_uno[1:6:2]
print(subtupla)

subtupla2 = tupla_uno[:6:2]
print(subtupla2)

#tupla_uno[1] = 11 #ESTO NO SE PUEDE, LAS TUPLAS NO PUEDEN MODIFICAR LOS VALORES DE LA MISMA
#print(tupla)

mitupla = ("Enero","Febrero","Marzo","Abril","Mayo")
uno,dos,tres,cuatro,cinco = mitupla[0],mitupla[1],mitupla[2],mitupla[3],mitupla[4]
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

print("*********")
uno,dos,tres,cuatro,cinto = mitupla #asignando toda la tupla a variables
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco)

print("*********")
mitupla2 = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")
uno, dos, tres, cuatro, *cinco = mitupla2
print(uno)
print(dos)
print(tres)
print(cuatro)
print(cinco) #en la variable "cinco" se crea una lista con el resto de elementos de la tupla

print("*********")
mitupla3 = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")
uno, dos, *tres, cuatro, cinco = mitupla3
print(uno)
print(dos)
print(tres) #en la variable "tres" se alojan los meses marzo, abril, mayo
print(cuatro)
print(cinco) 

print("*********")
mitupla4 = ("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio")
milista = [10,20,30,40,50]
objeto = zip(mitupla4,milista)
print(objeto)
objeto = tuple(objeto) #devuelve una tupla del objeto iterable zip
print(objeto)
objeto2 = zip(mitupla4,milista)
objeto2 = list(objeto2) #devuelve una lista del objeto iterable zip
print(objeto2)

print("*********")
nueva_lista = list(mitupla4) #convertir tupla a lista
print(nueva_lista)
nueva_tupla = tuple(milista) #convertir lista a tupla
print(nueva_tupla)

print("*********")
cadena = "Curso Python"
nueva_lista2 = list(cadena)
nueva_tupla2 = tuple(cadena)
print(nueva_lista2)
print(nueva_tupla2)