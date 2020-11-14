# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
# luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. 
# Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():

    def __init__(self,pLlantas,pColor,pPrecio):
        self.llantas = pLlantas
        self.color = pColor
        self.precio = pPrecio

    def __str__(self):
        return "El objeto creado es {} - {} - {}".format(self.llantas,self.color,self.precio)
        
###################

class Moto(Fabrica):
    pass

###################

class Carro(Fabrica):
    pass

###################

moto =  Moto(2,"Rojo",1000)
print(str(moto))
carro = Carro(4,"Negro",6000)
print(str(carro))