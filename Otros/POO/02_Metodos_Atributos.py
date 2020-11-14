# clase
class Persona():

    # atributos
    nombre = "Carlos"
    apellido = "Vergara"
    sexo = "Masculino"
    edad = 30

    # metodos
    def hablar(self, mensaje):
        return mensaje

###########################


# objeto
persona = Persona()

print(persona.hablar("Hola soy"), "{} y mi apellido es {}, tengo {} y de sexo {}".format(
    persona.nombre, persona.apellido, persona.edad, persona.sexo))
