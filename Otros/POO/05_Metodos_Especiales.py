class Persona():
    nombre = ""
    apellido = ""

    ## __init__ es el PRIMER METODO que se ejecuta en toda la clase
    ## sirve para inicializar los atributos de una clase
    ## vendría a ser el CONSTRUCTOR de la clase
    def __init__(self, pNombre, pApellido):
        self.nombre = pNombre
        self.apellido = pApellido
        print("El objeto {} {} ha sido creado".format(self.nombre,self.apellido))

    # es un símil al método toString de Java
    def __str__(self):
        return "El objeto tiene como atributo el nombre {} y el apellido {}".format(self.nombre,self.apellido)

    # metodo DESTRUCTOR, los objetos creados en memoria creados por init, 
    # lo elimina y lo reemplaza por otro
    def __del__(self):
        print("El objeto {} {} ha sido destruido".format(self.nombre,self.apellido))
        

persona = Persona("Juan","Perez")
print(str(persona))