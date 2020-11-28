#escriba un script que sea capaz de calcular el tiempo que demorará una persona en trasladarse de un lugar a otro.

distancia = float(input("Ingresa la distancia entre el origen y destino: "))
velocidad = float(input("Ingrese la velocidad a la que viajará: "))

tiempo = round(distancia/velocidad,2)

print("Usted llegará a destino en "+str(tiempo))