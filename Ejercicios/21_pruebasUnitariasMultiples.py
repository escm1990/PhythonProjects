#Función que calcula el área de un triángulo
def calcula_area(base,altura):
    """
    Comprobando el funcionamiento del script
    >>> calcula_area(10,5)
    'El área del triángulo es: 25.0'
    >>> calcula_area(9,5)
    'El área del triángulo es: 22.5'
    >>> calcula_area(10,6)
    'El área del triángulo es: 30.0'
    """
    return "El área del triángulo es: " + str((base*altura)/2)
import doctest
doctest.testmod()