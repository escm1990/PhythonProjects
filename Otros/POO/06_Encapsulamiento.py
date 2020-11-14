class A():
    def __init__(self):
        self.contador = 0
    def incrementar(self):
        self.contador += 1
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0 ## a un atributo, al ponerle el doble guion bajo está encapsulado, no puede ser ocupado FUERA de la clase B
    def incrementar(self):
        self.__contador += 1
    def cuenta(self):
        return self.__contador

a = A()
a.incrementar()
a.incrementar()
print(a.cuenta())
print(a.contador)

b = B()
b.incrementar()
b.incrementar()
print(b.cuenta())
# print(b.contador) # esta linea devuelve un error porque el atributo está ENCAPSULADO (solo visible dentro de su clase)
print(b._B__contador) # así se puede acceder a un atributo encapsulado dentro de una clase