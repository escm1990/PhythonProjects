class Persona():
    nombre = False

    ## __init__ es el PRIMER METODO que se ejecuta en toda la clase
    ## sirve para inicializar los atributos de una clase
    def __init__(self):
        print("Has creado el objeto Persona")

    ##self es un atributo que reemplaza a global, engloba las variables para que se usen en TODA la clase
    def datos(self): 
        self.nombre = True

##

# persona = Persona()
# persona.datos()
# print(persona.nombre)