lista = [5,9,1,58,4,2.65,10.8,9]

lista.sort() #orden ascendente
print(lista)

lista.sort(reverse=True) #orden descendente
print(lista)

valor = lista[0] #obtener el primer indice de la lista ordenada
print(valor)

minimo = min(lista)
print(minimo)

maximo = max(lista)
print(maximo)

longitud = len(lista)
print(longitud)

busqueda = 5 in lista #buscar un valor en una lista, devuelve un boolean
print(busqueda)

indice = lista.index(4) #devuelve la posicion del item en la lista
print(indice)

contar = lista.count(9) #cuenta el numero de veces que aparece el item
print(contar)