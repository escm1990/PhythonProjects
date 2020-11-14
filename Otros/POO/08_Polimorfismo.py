##Los metodos de las clases HIJAS pueden modificarse aunque en las clases PADRE ya estén definidas

class Animales():
    def __init__(self,nombre,mensaje):
        self.nombre = nombre
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)


class Perro(Animales): # HERENCIA EN PYTHON
    def hablar(self):
        print("Yo hago Guau!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

##############

perro = Perro("Firulais","Guau!")
perro.hablar()

# creando una lista de clases
listaAnimales = [Perro("Perrito","Guau2"),Pez("Nemo","nada")]
for i in listaAnimales:
    i.hablar()