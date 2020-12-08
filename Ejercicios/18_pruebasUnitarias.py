#a manera de ejemplo, si se deja 25 en lugar de 25.0 dará error en python, e imprimirá en pantalla

#Función que calcula el área de un triángulo
def calcula_area(base,altura):

    '''
    Comprobando el funcionamiento del script
    
    >>> calcula_area(10,5)
    25.0
    '''
    
    return (base*altura)/2

import doctest #importar módulo
doctest.testmod()