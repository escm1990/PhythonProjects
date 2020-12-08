'''
En otros lenguajes de programación son conocidos como
arreglos, arrays o vectores. En Python se conocen como
listas
'''

lista_participantes=["Francisco","Luis","Ana","Carlos","Juan"]
print(lista_participantes[:])
print("--------------------------------------------")
print(lista_participantes[2])
print("--------------------------------------------")
lista_participantes.append("Laura") #agrega el elemento al final
print(lista_participantes)
print("--------------------------------------------")
lista_participantes.insert(3,"Susana") #insert necesita 2 argumentos: el primero el indice y el segundo el item a agregar
print(lista_participantes)
print("--------------------------------------------")
lista_participantes.extend(["Ernesto","Fátima","Ruth","Pedro"]) # Agregar elementos
print(lista_participantes)
print("--------------------------------------------")
print(lista_participantes.index("Fátima")) #Buscar elementos; ¿dónde está Fátima?
print("--------------------------------------------")
lista_participantes=["Francisco","Luis","Ana",10,"Carlos","Juan",False]
lista_participantes.extend(["Ernesto","Fátima","Ruth","Pedro"])
print(lista_participantes.index)
print("--------------------------------------------")
lista_participantes.remove("Fátima") #Eliminar elementos
print("Fátima" in lista_participantes) #¿Fátima existe?
print(lista_participantes)
print("--------------------------------------------")
lista_participantes.pop() #elimina el último elemento
print(lista_participantes)
print("--------------------------------------------")
lista_participantes=["Francisco","Luis","Ana",10,"Carlos","Juan",False]
otra_lista_participantes=["Ernesto","Fátima","Ruth","Pedro"]
lista_final=lista_participantes+otra_lista_participantes #Unir listas.
print(lista_final)
print("--------------------------------------------")
lista_participantes=["Francisco","Luis","Ana",10,"Carlos","Juan",False] * 4 #Repetir listas.
print(lista_participantes)