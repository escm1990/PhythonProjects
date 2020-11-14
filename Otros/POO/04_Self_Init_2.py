class Persona():
    nombre = ""
    apellido = ""

    ## __init__ es el PRIMER METODO que se ejecuta en toda la clase
    ## sirve para inicializar los atributos de una clase
    def __init__(self, pNombre, pApellido):
        self.nombre = pNombre
        self.apellido = pApellido
        print("Has creado el objeto Persona llamado {} {}".format(pNombre,pApellido))
    

persona = Persona("Juan","Perez")