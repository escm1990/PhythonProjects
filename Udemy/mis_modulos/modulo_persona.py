class Persona:

    def __init__(self,nombre,edad):
        # el atributo sin guión después del self es public
        # el atributo con un guión después del self es protected
        # el atributo con doble guión después del self es privado (requiere crear métodos get/set) 
        self.__nombre = nombre
        self.__edad = edad

    def __str__(self):
        return "Nombre: " + self.__nombre + " Edad: "+ str(self.__edad)