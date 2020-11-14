# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos 
# el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, 
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():

    def __init__(self,pNombre,pNota):
        self.nombre = pNombre
        self.nota = pNota

    def imprimir(self):
        if(self.nota >= 7):
            print("El alumno {} aprobó con {}".format(self.nombre,self.nota))
        else:
            print("El alumno {} reprobó con {}".format(self.nombre,self.nota))


############

alu1 = Alumno("Juan",8)
alu2 = Alumno("Pedro",5)

alu1.imprimir()
alu2.imprimir()