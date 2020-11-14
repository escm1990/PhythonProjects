class Animales():
    def __init__(self,descripcion,especie,hablar):
        self.descripcion = descripcion
        self.especie = especie
        self.hablar = hablar

    def habla(self):
        print("Yo hago ",self.hablar)

    def describir(self):
        print("Soy de la especie ",self.especie)

class Perro(Animales): # HERENCIA EN PYTHON
    pass

class Abeja(Animales): #HERENCIA
    def sonido(self,sonido):
        self.sonido = sonido
        print(self.sonido)

##############

perro = Perro("Perro","Mamífero","Guau!")
perro.habla()
perro.describir()

abeja = Abeja("Abeja","Insecto","brr")
abeja.habla()
abeja.describir()
abeja.sonido("brr")