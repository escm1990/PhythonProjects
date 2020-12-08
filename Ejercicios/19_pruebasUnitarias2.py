#Función que calcula el área de un triángulo
def calcula_area(base,altura):
    '''
    Comprobando el funcionamiento del script
    >>> calcula_area(10,5)
    25
    '''
    return "El área del triángulo es: " + str((base*altura)/2)
    
import doctest
doctest.testmod()